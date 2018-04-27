import networkx as nx
import matplotlib.pyplot as plt
import random, time
import numpy as np
from source.student_utils_sp18 import *

def graph_from_file(infile):
    lines = []
    with open(infile) as f:
        for line in f:
            lines += [line.strip("\n")]
    size = int(lines[0])
    nodes = lines[1].split()
    source = lines[2]
    for i in range(len(nodes)):
        if nodes[i] == source:
            source_num = i

    mat = []
    whiteSpaceRegex = "\\s";
    
    for line in lines[3:]:
        mat += [line.replace("\t"," ") .split(" ")]

    g = adjacency_matrix_to_graph(mat)
    conquer_costs = [mat[i][i] for i in range(len(mat))]

    for i in range(len(g.nodes)):
        for j in range(len(g.nodes)):
            try:
                if g[i][j]['weight'] == "0":
                    g.remove_edge(i,j)
            except:
                continue

    mapping = dict(zip(range(size), nodes))
    nx.relabel_nodes(g, mapping, False)

    return g, conquer_costs, source

def output_to_file(file_name, path, conquered):
    path_str = " ".join(path)
    conquered_str = " ".join(conquered)

    with open(file_name, "w") as f:
        f.write(path_str)
        f.write("\n")
        f.write(conquered_str)


def display(g, source, edge_labels = True):
    colormap = {}
    for i in g.edges():
        if str(i) == source:
            colormap[i] = "b"
        else:    
            colormap[i] = "r"

    plt.figure(figsize=(15,7))

    labels = {}
    # for i in g.edges():
    #     labels[i] = int(g[i[0]][i[1]]['weight'])
    pos = nx.spring_layout(g)
    if edge_labels:
        nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)

    nx.draw(g,with_labels=True,font_size=10, pos = pos)

    # add node labels for conquer costs too
    plt.draw()
    plt.show()
    # mapping goes old to new, int to whatever is in source


