import networkx as nx
import numpy as np

g = nx.read_edgelist("facebook_combined.txt")
# the graph structure created need to be captured
N = list(g.nodes())
# takes list of nodes
spll = []# shortest path length list

for u in N:
     #capture another node to find shortest path
     for v in N:
         if u != v:
             l = nx.shortest_path_length(g, u, v)
             print("The shortest path between ",u," and ",v,"is ", l)
             spll.append(l)

min_spl = min(spll)
max_spl = max(spll)

avg_spl = np.average(spll)

print("Minimum shortest path length is ", min_spl)

print("Maximum shortest path length is ", max_spl)

print("Average  path length is ", avg_spl)
