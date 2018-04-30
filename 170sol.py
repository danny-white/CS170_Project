import networkx as nx
import matplotlib.pyplot as plt
import random, time
import numpy as np
from source.student_utils_sp18 import *
from source.local_utils import *
# import Christofides
ignored_nodes = []
g, conquer_costs, source = graph_from_file("inputs2/0.in")
print(g.nodes)
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
greedy_min_path(g, source)




# def min_2d_path(g, source, ignored_nodes):
# 	weights = {}
# 	for n in g.neighbors(source):
# 		if n in ignored_nodes:
# 			continue
# 		for nn in g.neighbors(n):
# 			if nn in ignored_nodes:
# 				continue
# 			weights[(source, n, nn)] = g[source][n]['weight'] + g[n][nn]['weight']
# 	ret = min(weights, key=weights.get)
	# return ret, weights[ret]
# print(min_2d_path(g, source, ignored_nodes))





# TSP = christofides.compute(distance_matrix)


# print(source)
# display(nx.dfs_tree(g, source), source)

# print(nx.maximal_independent_set(g, ["Hera"]))
# display(g, source)