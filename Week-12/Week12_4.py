import networkx as nx
import random
import matplotlib.pyplot as plt

def rank_by_points(points):
    dict_points = {}
    for i in range(len(points)):
        dict_points[i] = points[i]
    
    dict_points = sorted(dict_points.items(), key=lambda x : x[1])
    print(dict_points)

def assign_points(G):
    nodes = list(G.nodes())
    p = []
    for each in nodes:
        p.append(100)
    return p
 
def distribute_points(G, points):
    nodes = list(G.nodes())
    new_points = []
    
    for i in range(len(nodes)):
        new_points.append(0)
        
    for n in nodes:
        out = list(G.out_edges(n))
        if len(out) == 0:
            new_points[n] += points[n]
        else:
            share = points[n] / len(out)
            for (src, tgt) in out:
                new_points[tgt] += share
    
    return new_points
    
def keep_distributing(points, G): 
    while(1):
        new_points = distribute_points(G, points)
        print(new_points)
        points = new_points
        stop = input("Press # to stop or any other key to continue...")
        
        if stop == '#':
            break
        
    return new_points
    
G = nx.gnp_random_graph(10, 0.5, directed=True) 
nx.draw(G, with_labels = True)
plt.show()

#assign initial points
points = assign_points(G)

#keep distributing
final_points = keep_distributing(points, G) 

#rank by points
rank_by_points(final_points)


#default networkx function

b = nx.pagerank(G)
print(sorted(b.items(), key=lambda x : x[1]))