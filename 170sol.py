import networkx as nx
import matplotlib.pyplot as plt
import random, time
import numpy as np
from source.student_utils_sp18 import *
from source.local_utils import *
# import Christofides

g, conquer_costs, source = graph_from_file("inputs2/10.in")





# start at a node, iterate through all 2 deep paths out from the node, and take the shortest one. 
# Then Repeat from the end of the path you select in the previous stem
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 



def min_2d_path(g, source, ignored_nodes):
    weights = {}    
    for n in g.neighbors(source):
        if n in ignored_nodes:
            continue
        for nn in g.neighbors(n):
            if nn in ignored_nodes:
                continue
            weights[(source, n, nn)] = g[source][n]['weight'] + g[n][nn]['weight']
    ret = min(weights, key=weights.get)
    return ret, weights[ret]

def min_neighbor_conquer(g, source, conquer_costs):
    temp = {}
    for n in g.neighbors(source):
        temp[n] = conquer_costs[n]
    ret = min(conquer_costs, key=conquer_costs.get)
    return ret, conquer_costs[ret]

    

# display(nx.minimum_spanning_tree(g))


# TSP = christofides.compute(distance_matrix)


# print(source)


# print(nx.maximal_independent_set(g, ["Hera"]))
# display(g, source)