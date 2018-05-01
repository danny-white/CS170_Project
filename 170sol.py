import networkx as nx
import matplotlib.pyplot as plt
import random, time
import numpy as np
from source.student_utils_sp18 import *
from source.local_utils import *
from source.utils import *
# import Christofides


import os.path
for name in [str(i) for i in range(200,400)]:
    if not os.path.exists("outputs2/" + name + ".out"):
        print(name)
notrun = [
201,
203,
205,
210,
211,
212,
213,
214,
215,
219,
221,
229,
232,
237,
238,
239,
241,
243,
244,
245,
249,
250,
256,
257,
261,
262,
263,
267,
268,
269,
273,
274,
275,
276,
277,
278,
279,
280,
281,
283,
285,
286,
287,
292,
295,
301,
303,
304,
305,
306,
307,
308,
310,
312,
313,
314,
318,
319,
320,
321,
322,
323,
324,
325,
326,
333,
334,
335,
336,
337,
338,
339,
340,
341,
345,
346,
347,
349,
351,
352,
353,
355,
366,
367,
375,
376,
377,
382,
388,
394,
]

a,b = 350,400


# If neither the source nor target are specified return a dictionary 
# of dictionaries with path[source][target]=[list of nodes in path].
#display(g, source)

def distance(g, path):
    
    prev = None
    total = 0
    for i in path:
        if not prev:
            prev = i
        else:
            total += g[prev][i]['weight']
            prev = i
    return total

def make_path(nodes): 
    return list(nodes[1])

def has_leaves(g, node):
    # true if any surrounding nodes are leaves
    return any([1 if len(list(nx.neighbors(g,i))) == 1 else 0 for i in nx.neighbors(g,node)])
@timeout(30)
def build_tour(g, start):
    start_leaf = -1
    if len(set(g.neighbors(start))) == 1:
        for node in g.neighbors(start):
            if len(set(g.neighbors(node))) > 1:
                start_leaf = start
                start = node
                break
    core_nodes = set([])
    leaf_nodes = set([])
    for i in g.nodes():
        if len(set(g.neighbors(i))) > 1:
            core_nodes.add(i)
        else:
            leaf_nodes.add(i)


    size = len(core_nodes)        

    core_graph = g.copy()
    for leaf in leaf_nodes:
        core_graph.remove_node(leaf)

    short_paths = nx.shortest_path(core_graph, weight="weight")
    edges = set([])
    edge_map = {}
    for source in short_paths:
        for dest in short_paths:
            if source != dest and (dest, source) not in edge_map:
                edge_map[(source, dest)] = ((source, dest),tuple(short_paths[source][dest]), distance(core_graph, short_paths[source][dest]))
                edges.add(((source, dest),tuple(short_paths[source][dest]), distance(core_graph, short_paths[source][dest])))
    
    

    tour = nx.Graph()
    # find cycle 
    # ensure no edge has degree > 2 

    edge_ref = edges.copy()
    while (len(tour.edges()) < size ):

        new_edge = min(edge_ref, key=lambda p: p[2])
        edge_ref.remove(new_edge)

        tour.add_edge(new_edge[0][0], new_edge[0][1], weight=new_edge[2])
        try:
            if nx.find_cycle(tour) and len(tour.edges()) < size:
                # print("fail1")
                tour.remove_edge(new_edge[0][0], new_edge[0][1])
                continue
        except: 
            pass
        
        for i in tour.nodes():
            if len(list(nx.neighbors(tour, i))) > 2:
                # print("fail")
                tour.remove_edge(new_edge[0][0], new_edge[0][1]) 
                
        # exit()
    remap = {}
    for e in tour.edges():
        if e not in g.edges():
            try:
                remap[(e[1], e[0])] = edge_map[(e[1], e[0])]
            except:
                remap[(e[0], e[1])] = edge_map[(e[0], e[1])]
            # print(edge_map[e[0]][e[1]])
            # print(edge_map[e[1]][e[0]])
    path = list(nx.dfs_preorder_nodes(tour, start))
    path.append(path[0])
    if start_leaf == -1:
        final = []
    else:
        final = [start_leaf]
    prev = None
    for e in path:
        if not prev:
            final.append(e)
            prev = e
            continue

        if (prev,e) in remap:
            final += make_path(remap[(prev,e)])[1:]
            prev = e
        elif (e,prev) in remap:
            final += make_path(remap[(e,prev)])[::-1][1:]
            prev = e
        else:
            final.append(e)
            prev = e
    if start_leaf != -1:
        final.append(start_leaf)
    return final
    # tour =
    # exit() 
    # display(g, source)
    

    # now short_paths is the complete graph, we thus take the smallest edge in it, 
    # verify it doesnt break the 2 vertex / cycle thing and repeat
@timeout(10)
def generate_conquering(g, walk):
    conquered = dict(zip(list(g.nodes), [0 for i in g.nodes()]))
    followers = dict(zip(list(g.nodes), [0 for i in g.nodes()]))
    for e in walk:
        if has_leaves(g, e):
            conquered[e] = 1
            followers[e] = 1
            for node in nx.neighbors(g,e):
                followers[node] = 1
    # followers is now a dict of fallen nodes
    # take the ones that are not fallen, rank them based on the cost function and then conquer the best one and recalc
    costs = []
    for i in followers:
        if not followers[i]:
            costs.append(i)

    while not all(followers.values()):
        # conquer something
        next_conq = max(costs, key=lambda p: cost(g, p, followers))
        conquered[next_conq] = 1
        followers[next_conq] = 1
        for node in nx.neighbors(g,next_conq):
            followers[node] = 1
        # re calculate the costs of every node
        costs = {}
        for i in followers:
            if not followers[i]:
                costs[i] = cost(g, i, followers)    
    return conquered

def cost(g, node, followers):
    this_cost = conquer_costs[node]
    neighbor_costs = sum([(conquer_costs[i] + g[node][i]['weight']) if not followers[i] else 0 for i in nx.neighbors(g, node)])
    return neighbor_costs / this_cost

def get_sol(g, path, conq):
    for e in g.nodes():
        g.nodes()[e]['weight'] = float(g.nodes()[e]['weight'])
    return cost_of_solution(g, path, conq)

# for name in [str(i) for i in range(100)]:

for name in [str(i) for i in range(a,b)]:
    try: 
        if not (int(name) % 10):
            print(name)
        g, conquer_costs, source = graph_from_file("inputs2/" + "50" + ".in")
        t = build_tour(g, source)
        clist = generate_conquering(g,t)
        conq = set([i for i in clist.keys() if clist[i]])

        file = "outputs2/" + name  + ".out"
        output_to_file(file, t, list(conq))

        # print(get_sol(g, t, conq))
    except Exception as e:
        print(e)
        print(name)

#for name in [str(i) for i in range(a,b)]:
for name in [str(i) for i in notrun]:
    try: 
        print(name)
        g, conquer_costs, source = graph_from_file("inputs2/" + name + ".in")
        t = build_tour(g, source)
        clist = generate_conquering(g,t)
        conq = set([i for i in clist.keys() if clist[i]])

        file = "outputs2/" + name  + ".out"
        output_to_file(file, t, list(conq))

        # print(get_sol(g, t, conq))
    except Exception as e:
        write_to_file("errorlog.txt", str(e) + "\n" + str(name))

