import networkx as nx
import random
import matplotlib.pyplot as plt

def add_edges():
    nodes = list(G.nodes())
    for s in nodes:
        for t in nodes:
            if s!=t: # skip checking themselves
                r = random.random()
                if r <= 0.5: # randomly add edges assuming tossing coin
                    G.add_edge(s,t)
    return G

def assign_points(G):
    nodes = list(G.nodes())
    p = []
    for each in nodes:
        p.append(100) # we assume seed value as 100
    return p

def distribute_points(G, points):
    nodes = list(G.nodes())
    new_points = []
    for i in range(len(nodes)): #initialising point list
        new_points.append(0)

    for n in nodes:
        out = list(G.out_edges(n))
        if len(out) == 0: # no outgoing edges hence no sharing
            new_points[n] = new_points[n] + points[n] # 0 + old points
        else:
            share = points[n]/len(out) # equal distribution of points
            for (src,tgt) in out:
                new_points[tgt] = new_points[tgt] + share
    return new_points 

def keep_distributing(points, G):
    while(1):
        new_points = distribute_points(G, points)
        print("\n",new_points)
        points = new_points
        stop = input("\nPress # to stop and any other key to continue")
        if stop == "#":
            break
    return new_points

def rank_by_points(points):
    d = {}
    for i in range(len(points)):
        d[i] = points[i]
    print("\nPoint distribution method for pagerank :-\n\n",sorted(d.items(),key = lambda x:x[1]))

#create a directed graph
G = nx.DiGraph()
G.add_nodes_from([i for i in range(10)])
G = add_edges()

#Visualize thr graph
nx.draw(G, with_labels = True)
plt.show()

#assign initial points
points = assign_points(G)

# keep distributing
final_points = keep_distributing(points, G) # when we final points are acheived
# ie when user breaks while loop

rank_by_points(final_points)

#default pagerank function in networkx function to verify our work
result = nx.pagerank(G)
print("\nNetworkx pagerank :-\n\n",sorted(result.items(),key = lambda x:x[1]))

