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
with open("200.in") as f:
    for line in f:
        lines += [line.strip("\n")]
size = lines[0]
nodes = lines[1].split()
source = lines[2]
for i in range(len(nodes)):
    if nodes[i] == source:
        source_num = i

mat = []
for line in lines[3:]:
    mat += [line.split(" ")[0:-1]]



# def dumb_solution(mat, source):
#     visited = []
#     curr_walk = ""
#     for nodes in source:
#         if cost exists:
#             visited.append(node)

source = 99


gg = adjacency_matrix_to_graph(mat)

for i in range(len(gg.nodes)):
    for j in range(len(gg.nodes)):
        try:
            if gg[i][j]['weight'] == "0":
                gg.remove_edge(i,j)
        except:
            continue
print(len(gg.edges))
tree = nx.dfs_tree(gg, source) #graph
succ = nx.dfs_successors(gg, source) #dict
pred = nx.dfs_predecessors(gg, source) #dict

pre_num = list(nx.dfs_preorder_nodes(gg,source))
pre = [names[i] for i in pre_num]

for i in pre_num:
    try:
        succ[i]
    except:
        print(names[i])

print("parents")
print(names[pred[names.index("gn")]])
print(names[pred[names.index("gm")]])
# print(pre)
print("asdasdasdas")
t = "gp"
while 1:
    print(t, end = " ")
    t = names[pred[names.index(t)]]
exit()

print("asdoias")

asd = []
ttt = "cv c a d h b e j f k g i l p m r n o v q s x t w ac y u z aa ap ab ae ag ai ak ad af al aj at am an ah as aw aq au ar ao ba be ax bb bc bf av ay bg bh bk az bd bi bj bt bl bv bm bn bo bp bq bs bz by br bu bw ca cb ce cc cd cf bx ch cn cg cm ck ci cj cq cl cy co cr ct cp cs cw cu cz da dd cx db df dg dc de dh dn dk di dl dm do dv dj ds dr dp dt dw dq ea du dx ef ee dy dz eh eb eg ed ei ej ec em el ek eo ep en eq eu es ew er et ev ex ez ey fa fc fd fh fb fj fg ff fl fk fr fi fe fm fo fn fu ga fp fq fv fw ft fs fz fx fy gc gd gg gb gh ge gl gr gi gf go gf gj gm gj gn gq gk gq gp".split(" ")
for i in range(len(ttt)):
    if i %2 == 0:
        asd.append(ttt[i])
print(set(asd))



# def dumb_dfs(source):
#     walk = []
#     queue = [source]
#     while len(queue) != 0:
#         curr_node = queue.pop()
#         walk.append(curr_node)
        
#         if curr_node not in succ:
#             walk.append(pred[curr_node])
#         else:
#             for node in succ[curr_node]:
#                 queue.append(node)
#     end = walk[-1]
#     while 1:
#         try:
#             walk.append(pred[end])
#             end = pred[end]
#         except:
#             break
#     return walk

# res = dumb_dfs(source)
# for j in [names[i] for i in res]:
#     print(j, end = " ")
# print()
# print("```````")
# conc = []
# for j in [names[i] for i in res if i %2 == 0]:
#     conc.append(j)
# print(set(conc))

# while 1:
#     a = input(">>")
#     a = names.index(a)
#     try: 
#         p = names[pred[a]]
#     except:
#         p = "none"
#     try:
#         s = [names[i] for i in succ[a]]
#     except:
#         s= "none"
#     print("succ =" + str(s))
#     print("pred =" + str(p))


# nx.draw(tree,with_labels=True)
# plt.draw()
# plt.show()

