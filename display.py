import networkx as nx
import matplotlib.pyplot as plt
import random, time
import numpy as np
from source.student_utils_sp18 import *
from source.local_utils import *
g, conquer_costs, source = graph_from_file("inputs2/545.in")
for node in g.nodes:
	print(node)
	print(g[node])
print(conquer_costs)