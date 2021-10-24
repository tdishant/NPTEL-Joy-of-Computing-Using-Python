import networkx as nx
import random
import matplotlib.pyplot as plt
import operator

G = nx.gnp_random_graph(10, 0.5, directed=True)
nx.draw(G, with_labels = True)
plt.show()

#picking a node randomly from the given set of nodes
x = random.choice([i for i in range(G.number_of_nodes())])

dict_counter = {}
#initializing the dictionary to zeros
for i in range(G.number_of_nodes()):
    dict_counter[i] = 0

#incrementing the counter of x
dict_counter[x] += 1

#traverisng over the entire graph 100 times
for i in range(100):
    #list of all the neighbours of the current node
    list_n = list(G.neighbors(x))
    
    #now we check if the choen node is a sink or not i.e len(list_n) = 0
    if(len(list_n) == 0):
        x = random.choice([i for i in range(G.number_of_nodes())])
    else:
        x = random.choice(list_n)
    dict_counter[x] += 1
    
#there is also a built in function in networkx that gives the pagerank values of all the nodes so we can verify our algo
p = nx.pagerank(G)
sorted_p = sorted(p.items(), key=operator.itemgetter(1))
print(sorted_p)
#sorted_rw = sorted(dict_counter.items(), key=operator.itemgetter(1))
sorted_rw = sorted(dict_counter.items(), key=lambda x : x[1])
print(sorted_rw)