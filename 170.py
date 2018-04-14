# generate an adjacency list of an n-node graph

# constraints for any triangle in the graph the triangle must satsify the triangle inequality
# less than N nodes
# format: Cii = cost of conquering, Cij is time to go from i to j = Cji, undirected graph, "x" implies no edge
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


def is_metric(G):
    shortest = dict(nx.floyd_warshall(G))
    for u, v, datadict in G.edges(data=True):
         if shortest[u][v] != datadict['weight']:
            return False
    return True

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



