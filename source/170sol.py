import networkx as nx
import matplotlib.pyplot as plt
import random, time
import numpy as np
from names import *
from student_utils_sp18 import *



###########################
###########################
##                       ##
######## THIS CODE ########
##### IS REALLY DUMB ######
###### DON'T USE IT #######
##                       ##
###########################
###########################




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

