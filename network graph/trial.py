import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
# initialising graph
g.add_nodes_from([1,2,3,4,5,6,7,8])
g.add_node(9)

g.add_edges_from([(1,2),(2,4),(1,9),(4,7),(6,8),(5,6),(8,9)])
g.add_edge(2,9)

nx.draw(g)
plt.show()

print("degree of 2 in the graph is ",g.degree(2))

g = nx.gnp_random_graph(20,0.5)

nx.draw(g)
plt.show()

g = nx.barabasi_albert_graph(50,5)

nx.draw(g)
plt.show()
nx.write_gexf(g, "analysis1.gexf")
