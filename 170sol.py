import networkx as nx
import matplotlib.pyplot as plt
import random, time
import numpy as np
from source.student_utils_sp18 import *
from source.local_utils import *
# import Christofides

g, conquer_costs, source = graph_from_file("inputs2/364.in")



# TSP = christofides.compute(distance_matrix)


# print(source)
# display(nx.dfs_tree(g, source), source)

# print(nx.maximal_independent_set(g, ["Hera"]))
# display(g, source)