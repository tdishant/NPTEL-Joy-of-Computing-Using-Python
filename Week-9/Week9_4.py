import networkx as nx
import numpy as np
#to read the edge list
G = nx.read_edgelist("facebook_combined.txt")
N = list(G.nodes())

#to store the length of the shortest path between tow nodes
spll = []

#reading all the nodes pairwise

for u in N:
    for v in N:
        if u != v:
            #length of the shortest path
            l = nx.shortest_path_length(G, u, v)
            print(l)
            spll.append(l)
        
#minimun shortest path length
min_spl = min(spll)
max_spl = max(spll)

avg_spl = np.average(spll)
