import networkx as nx
import random
import matplotlib.pyplot as plt
import operator

G = nx.gnp_random_graph(10, 0.5, directed = True)
# directed grpah meaning with arrowheads which is essential in our case
#

nx.draw(G, with_labels = True)# labels indicate naming of a node
plt.show()

x = random.choice([i for i in range(G.number_of_nodes())])
# x is the random source node

dict_counter = {}

for i in range(G.number_of_nodes()): # intialising the dict
    dict_counter[i] = 0
dict_counter[x] = dict_counter[x] + 1
# starting node gets 1 point
for i in range(1000000): # more the iterations nearer to  correct result
    list_n = list(G.neighbors(x))
    if len(list_n) == 0:
        x = random.choice([i for i in range(G.number_of_nodes())])
        # since last node was a sink hence selecting a new node randomly
        dict_counter[x] = dict_counter[x] + 1

    else:
        x = random.choice(list_n)# choose a node randomly
        dict_counter[x] = dict_counter[x] + 1

p = nx.pagerank(G)
# this function of networkx helps us verify if our appliction of random alki
# is orrect or not

sorted_p = sorted(p.items(), key = operator.itemgetter(1))
# sorts dictionary based on index 1 of p.items i.e values

sorted_rw = sorted(dict_counter.items(), key = operator.itemgetter(1))

#print(p)
#print(dict_counter)

#sorted dictionary based on values to get the picture more clearly

print(sorted_p)
print(sorted_rw)
