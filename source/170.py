# generate an adjacency list of an n-node graph

# constraints for any triangle in the graph the triangle must satsify the triangle inequality
# less than N nodes
# format: Cii = cost of conquering, Cij is time to go from i to j = Cji, undirected graph, "x" implies no edge
import networkx as nx
import matplotlib.pyplot as plt
import random, time
import numpy as np
from student_utils_sp18 import *
from names import *

def build(nodes, max, density):
    G = nx.Graph()
    m = n = nodes
    # add nodes:
    for i in range(n):
        G.add_node(names[i]);
    # add edges, randomly

    for i in range(n):
        for j in range(m):
            if random.random() <= density and i != j:
                G.add_edge(list(G.nodes)[i],list(G.nodes)[j], weight = random.randint(max/2 + 1,max))
                # G.add_edge(list(G.nodes)[i],list(G.nodes)[j], weight = 1)

    assert(is_metric(G))
    assert(nx.is_connected(G))
    return G

def make_adj(graph, weights):
    ret = ""
    n = m = len(graph.nodes)
    for i in range(n):
        for j in range(m):
            if i == j:
                
                ret += str(weights[i]) + " "
            else:
                try:
                    
                    ret += str(g[list(g.nodes)[i]][list(g.nodes)[j]]['weight']) + " "
                except:
                    
                    ret += "x "
        ret += "\n"
    return ret


nodes = 200
max_time =10000
density = .2

weights = [random.randint(0,max_time) for i in range(nodes)]

g = build(nodes,max_time, density)
print(len(g.nodes))

for i in range(len(g.nodes)):
    print(list(g.nodes)[i], end=" ")
print()
print(list(g.nodes)[random.randint(0,len(g.nodes) - 1)])
a = make_adj(g, weights)
print(a, end="")

# mat = []
# for line in a.splitlines():
#     mat += [line.split(" ")[0:-1]]


nx.draw(g,with_labels=True)
plt.draw()
plt.show()


# gg = adjacency_matrix_to_graph(mat)
# nx.draw(gg,with_labels=True)
# plt.draw()
# plt.show()



