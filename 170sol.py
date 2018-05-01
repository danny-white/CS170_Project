import networkx as nx
import matplotlib.pyplot as plt
import random, time
import numpy as np
from source.student_utils_sp18 import *
from source.local_utils import *
# import Christofides
ignored_nodes = []
g, conquer_costs, source = graph_from_file("inputs2/0.in")

# If neither the source nor target are specified return a dictionary 
# of dictionaries with path[source][target]=[list of nodes in path].
#display(g, source)

def greedy_min_path(g, source):
	total_cost = float('inf')
	for node in g.nodes:
		dimension_graph = len(g.nodes)
		curr_cost = 0
		result_path = []
		count_num_nodes_in_walk = 0
		while count_num_nodes_in_walk < dimension_graph:
			local_cost = float('inf')
			for node_2 in g.nodes:
				if node != node_2 and node_2 in g[node]:
					print(node)
					print(node_2)
					index = node_2
					local_cost = int(g[node][node_2]['weight'])
					print(local_cost)
			curr_cost += local_cost
			result_path.append(g.nodes[node_2])	
			node = node_2 
		if curr_cost < total_cost:
			total_cost = curr_cost
	print(total_cost)
	print(result_path)
	return total_cost

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

def build_tour(g, start):
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
    final = []
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
    return final
    # tour =
    # exit() 
    # display(g, source)
    

    # now short_paths is the complete graph, we thus take the smallest edge in it, 
    # verify it doesnt break the 2 vertex / cycle thing and repeat

print(build_tour(g, "Ares") )
display(g, source)

def greedy_min_path(g, source):
    total_cost = float('inf')
    start = source
    paths = {}
    dimensions = len(g.nodes)
    for node in g[start]:
        dimension_graph = len(g.nodes)

        result_path = [start, node]
        for node_2 in g[node]:
            result_path.append(node_2)
            cost = g[start][node]['weight'] + g[node][node_2]['weight']
            paths[str(result_path)] = cost
        # if curr_cost < total_cost:
        #     total_cost = curr_cost
    print(total_cost)
    print(result_path)
    return total_cost 

def min_2d_path(g, source, ignored_nodes):
    weights = {}
    ignored_nodes.append(source)
    for n in g.neighbors(source):

        if n in ignored_nodes and g.neighbors(n) > 1:
            continue
        for nn in g.neighbors(n):
            if nn in ignored_nodes:
                continue
            weights[(source, n, nn)] = g[source][n]['weight'] + g[n][nn]['weight']
    ret = min(weights, key=weights.get)
    return ret, ret[2]
#min_2d_path(g, source, ignored_nodes)

def run(g, source):
	ignored_nodes = []
	viewed_nodes = []
	ret = []
	sub_path, last_point = min_2d_path(g, source, ignored_nodes)
	ret.append(sub_path)
	for i in sub_path:
		viewed_nodes.append(i)
		viewed_nodes.extend(g.neighbors(i))
	print(sub_path)
	print(last_point)
	while set(viewed_nodes) != g.nodes:
		sub_path, last_point = min_2d_path(g, last_point, ignored_nodes)
		for i in sub_path:
			viewed_nodes.append(i)
			viewed_nodes.extend(g.neighbors(i))
		print(sub_path)
		print(last_point)
		print("missing nodes")
		print(list(set(g.nodes) - set(viewed_nodes)))
		print(ret)
		ret.append(sub_path)
	return ret
# print(run(g, source))
def min_neighbor_conquer(g, source, conquer_costs):
    temp = {}
    for n in g.neighbors(source):
        temp[n] = conquer_costs[n]
    ret = min(conquer_costs, key=conquer_costs.get)
    return ret, conquer_costs[ret]
