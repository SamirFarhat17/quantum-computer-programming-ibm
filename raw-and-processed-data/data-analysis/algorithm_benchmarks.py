import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_historgram(X, data, groupings, name, title):
    to_add = {}
    for i in range(0, len(data)):
        to_add[groupings[i]] = data[i]

    df = pd.DataFrame(to_add, index=X)
    ax = df.plot.bar(rot=0)
    plt.xlabel("Nodes")
    plt.ylabel("Time (ms)")
    plt.savefig(name)
    plt.title(title)
    plt.show()


# Knapsack
knap_max_weights = [2, 4, 8, 16]
knap_types = ["qubo", "grover", "qaoa", "vqe"]

knap_vals_qubo = [13.3, 14.0, 13.4, 12.4]
knap_vals_grover = [117, 255, 214, 166]
knap_vals_qaoa = [176, 230, 318, 383]
knap_vals_vqe = [144, 165, 211, 232]
knap_all = [knap_vals_qubo, knap_vals_grover, knap_vals_qaoa, knap_vals_vqe]

#plot_historgram(knap_max_weights, knap_all, knap_types, "algos/knapsack.png", "Knapsack benchmarks with different weight counts")

# Maxcut
maxcut_degrees = [3, 5, 7, 9]
maxcut_types = ["qubo", "10x(grover)", "qaoa", "vqe"]

maxcut_vals_qubo = [11.5, 14.2, 20, 23.2]
maxcut_vals_grover = [8.52, 12.1, 11.66, 11.0]
maxcut_vals_qaoa = [271, 348, 425, 539]
maxcut_vals_vqe = [293, 311, 375, 380]
maxcut_all = [maxcut_vals_qubo, maxcut_vals_grover, maxcut_vals_qaoa, maxcut_vals_vqe]

#plot_historgram(maxcut_degrees, maxcut_all, maxcut_types, "algos/maxcutsack.png", "Maxcuts benchmarks with 12 nodes at different degrees")

# Vertex-cover
vc_degrees = [3, 5, 7, 9]
vc_types = ["qubo", "10x(grover)", "qaoa", "vqe"]

vc_vals_qubo = [12.2, 16.1, 18.0, 21.4]
vc_vals_grover = [7.56, 8.72, 11.1, 10.6]
vc_vals_qaoa = [394, 477, 571, 656]
vc_vals_vqe = [358, 412, 469, 475]
vc_all = [vc_vals_qubo, vc_vals_grover, vc_vals_qaoa, vc_vals_vqe]

#plot_historgram(vc_degrees, vc_all, vc_types, "algos/vertex_cover.png", "Vertex cover benchmarks with 12 nodes at different degrees")

# Docplex
lower_bound = ['lower bound -4', 'lower bound -3', 'lower bound -2', 'lower bound -1']
upper_bound = [2, 3, 4, 5]

lb_4 = [1.62, 1.57, 1.57, 1.54]
lb_3 = [1.52, 1.64, 1.58, 1.61]
lb_2 = [2.08, 1.53, 1.57, 1.66]
lb_1 = [1.58, 1.62, 1.59, 1.58]
lb_all = [lb_4, lb_3, lb_2, lb_1]

#plot_historgram(upper_bound, lb_all, lower_bound, "algos/docplex.png", "Docplex benchmarks for qubo at different ranges")

# Clique
clique_nodes = [5, 10, 17]
clique_types = ["2-degrees", "4-degrees", "8-degrees", "16-degrees"]

clique_vals_2 = [122, 420, 1570]
clique_vals_4 = [85, 354, 1410]
clique_vals_8 = [0, 233, 1086]
clique_vals_16 = [0, 0, 386]
clique_all = [clique_vals_2, clique_vals_4, clique_vals_8, clique_vals_16]

#plot_historgram(clique_nodes, clique_all, clique_types, "algos/clique.png", "Clique benchmarks different node degree combinations")
'''clique_nodes = [5, 10, 17]
clique_types = ["2-degrees", "4-degrees", "8-degrees", "16-degrees"]

clique_vals_2 = [8.33, 17.5, 41.6]
clique_vals_4 = [6.05, 14.7, 36.9]
clique_vals_8 = [0, 9.24, 27.7]
clique_vals_16 = [0, 0, 7.79]
clique_all = [clique_vals_2, clique_vals_4, clique_vals_8, clique_vals_16]'''

#plot_historgram(clique_nodes, clique_all, clique_types, "algos/clique_startup.png", "Clique converter benchmarks at different node degree combinations")

# Protein Folding

