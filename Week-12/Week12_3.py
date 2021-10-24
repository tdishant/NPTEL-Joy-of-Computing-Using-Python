import networkx as nx
'''
U = nx.gnp_random_graph(5, 0.5)
nx.draw(U)

D = nx.gnp_random_graph(5, 0.5, directed=True)
nx.draw(D)
'''
#to create undirected graph
U = nx.Graph()
#to create directed graph
D = nx.DiGraph()
#to add nodes in the graph
D.add_nodes_from([i for i in range(5)])
#to see the nodes of the graph
print(D.nodes())
#adding edges in the graph
D.add_edge(1, 2)
D.add_edge(0, 3)
D.add_edge(2, 3)
D.add_edge(3, 2)
D.add_edge(3, 4)
D.add_edge(4, 1)

print(D.out_edges(1))
print(D.out_edges(2))
print(D.out_edges(3))
print(D.in_edges(3))
print(D.in_edges(1))