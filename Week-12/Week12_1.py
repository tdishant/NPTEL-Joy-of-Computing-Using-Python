import networkx as nx

#two communities with 4 nodes each with 2 nodes in between 

'''G = nx.barbell_graph(4, 2)
nx.draw(G)

F = nx.barbell_graph(4, 3)
nx.draw(F)

H = nx.complete_graph(4)
nx.draw(H)

I = nx.cycle_graph(5)
nx.draw(I)

J = nx.ladder_graph(5)
nx.draw(J)

K = nx.path_graph(6)
nx.draw(K)
'''
L = nx.star_graph(6)
nx.draw(L)
'''
M = nx.wheel_graph(6)
nx.draw(M)

#(no of edges, probability of edge between two nodes)
N = nx.gnp_random_graph(5, 0.5)
nx.draw(N)'''