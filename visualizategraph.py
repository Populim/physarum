import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

M = np.loadtxt('matrix.txt')
G = nx.from_numpy_matrix(M)

positions = {0: [1,10], 1: [1,12], 2: [1,14], 3: [5,12],
 4: [7,14], 5: [8, 1], 6: [8, 3], 7: [9, 5],
  8: [9, 6], 9: [9, 8], 10: [9,14], 11: [11, 5], 12: [11, 6],
   13: [11,14], 14: [11,16], 15: [13, 8], 16: [13,14], 17: [15, 1],
    18: [15, 3], 19: [15, 7], 20: [15, 9], 21: [15,16]}


rotate = [[0,2],[-1,0]]
for k in positions.keys():
	v = positions[k]
	positions[k] = [v[1],-v[0]]


edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, pos=positions)
nx.draw_networkx_edge_labels(G,pos=positions,font_size=8,edge_labels=edge_labels)
plt.show()