import networkx as nx
import matplotlib.pyplot as plt

"""plot the graph when nodes pair source and target are provided in file"""
G = nx.read_edgelist("./rank.txt",create_using = nx.DiGraph(), nodetype = int)
nx.draw(G, with_labels =True)
plt.show()
