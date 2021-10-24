import networkx as nx
import matplotlib.pyplot as plt
'''
#to create a random graph with 50 nodes and 0.3 probability of having an 
#edge between two nodes

G = nx.gnp_random_graph(50, 0.3)

nx.draw(G)
plt.show()

print(G.nodes())
print(G.edges())

print(G.degree(0))
'''
#each node is coming with 2 edges, higher probability of connecting 
#to a node with higher degree

G = nx.barabasi_albert_graph(50, 2)
nx.draw(G)
plt.show()

nx.write_gexf(G, "analysis1.gexf")
