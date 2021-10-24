import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist("page_rank.txt", create_using = nx.DiGraph(), nodetype = int)
nx.draw(G, labels = True)
plt.show()