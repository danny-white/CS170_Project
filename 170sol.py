import networkx as nx
import matplotlib.pyplot as plt
import random, time
import numpy as np


names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] \
+ ['aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao', 'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'ax', 'ay', 'az'] \
+ ['ba', 'bb', 'bc', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bk', 'bl', 'bm', 'bn', 'bo', 'bp', 'bq', 'br', 'bs', 'bt', 'bu', 'bv', 'bw', 'bx', 'by', 'bz'] \
+ ['ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'cg', 'ch', 'ci', 'cj', 'ck', 'cl', 'cm', 'cn', 'co', 'cp', 'cq', 'cr', 'cs', 'ct', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz'] \
+ ['da', 'db', 'dc', 'dd', 'de', 'df', 'dg', 'dh', 'di', 'dj', 'dk', 'dl', 'dm', 'dn', 'do', 'dp', 'dq', 'dr', 'ds', 'dt', 'du', 'dv', 'dw', 'dx', 'dy', 'dz'] \
+ ['ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'eg', 'eh', 'ei', 'ej', 'ek', 'el', 'em', 'en', 'eo', 'ep', 'eq', 'er', 'es', 'et', 'eu', 'ev', 'ew', 'ex', 'ey', 'ez'] \
+ ['fa', 'fb', 'fc', 'fd', 'fe', 'ff', 'fg', 'fh', 'fi', 'fj', 'fk', 'fl', 'fm', 'fn', 'fo', 'fp', 'fq', 'fr', 'fs', 'ft', 'fu', 'fv', 'fw', 'fx', 'fy', 'fz'] \
+ ['ga', 'gb', 'gc', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gj', 'gk', 'gl', 'gm', 'gn', 'go', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gv', 'gw', 'gx', 'gy', 'gz']

def adjacency_matrix_to_graph(adjacency_matrix):
    node_weights = [adjacency_matrix[i][i] for i in range(len(adjacency_matrix))]
    adjacency_matrix_formatted = [[0 if entry == 'x' else entry for entry in row] for row in adjacency_matrix]
    
    for i in range(len(adjacency_matrix_formatted)):
        adjacency_matrix_formatted[i][i] = 0
    
    G = nx.convert_matrix.from_numpy_matrix(np.matrix(adjacency_matrix_formatted))
    
    for node, datadict in G.nodes.items():
        assert node_weights[node] != 'x', 'The conquering cost of node number {} was specified to be x. Conquering costs cannot be x.'.format(node)
        datadict['weight'] = node_weights[node]
    
    return G



lines = []
with open("50.in") as f:
    for line in f:
        lines += [line.strip("\n")]
size = lines[0]
nodes = lines[1].split()
source = lines[2]

mat = []
for line in lines[3:]:
    mat += [line.split(" ")[0:-1]]


gg = adjacency_matrix_to_graph(mat)

print(nx.find_cycle(gg))
nx.draw(gg,with_labels=True)
plt.draw()
plt.show()


exit()

mat = []
for line in a.splitlines():
    mat += [line.split(" ")[0:-1]]