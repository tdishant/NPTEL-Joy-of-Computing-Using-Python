import networkx as nx
import matplotlib.pyplot as plt
'''
#graph crated but empty
G = nx.Graph()
#to ad a node
G.add_node(1)
G.add_node(2)
G.add_node(3)
#to add the edges 
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

#to print nodes
print(G.nodes()) 
#to print edges
print(G.edges())

#to plot the graph
nx.draw(G)
plt.show()
'''
'''
G = nx.Graph()
#list of nodes
l = [1, 2, 3]   
G.add_nodes_from(l)
'''
#to create a complete graph of 10 nodes

G = nx.complete_graph(10)
nx.draw(G)
plt.show()


