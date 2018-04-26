import networkx as nx
import matplotlib.pyplot as plt
import random, time
import numpy as np
from names import *
from student_utils_sp18 import *
from local_utils import *


g, conquer_costs = graph_from_file("inputs/50.in")


print(conquer_costs)
exit()
nx.draw(g,with_labels=True)
plt.draw()
plt.show()
# mapping goes old to new, int to whatever is in source
