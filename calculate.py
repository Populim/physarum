import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import time


np.set_printoptions(precision=3,suppress=True,linewidth=np.inf)

positions = {0: [1,10], 1: [1,12], 2: [1,14], 3: [5,12],
 4: [7,14], 5: [8, 1], 6: [8, 3], 7: [9, 5],
  8: [9, 6], 9: [9, 8], 10: [9,14], 11: [11, 5], 12: [11, 6],
   13: [11,14], 14: [11,16], 15: [13, 8], 16: [13,14], 17: [15, 1],
    18: [15, 3], 19: [15, 7], 20: [15, 9], 21: [15,16]}

for k in positions.keys():
	v = positions[k]
	positions[k] = [v[1],-v[0]]


def functionQ(x):
	return np.power(abs(x),1.3)

def systemDynamics(Q,D):
	for i in range(Q.shape[0]):
		for j in range(Q.shape[0]):
			D[i,j] = D[i,j] + (functionQ(Q[i,j]) - D[i,j]) * 0.05
			#if((i == 6 or i==5) and j == 0):
				#print(functionQ(Q[i,j]) - D[i,j], i, j, D[i,j])
	return D





source = 17
sink = 20

#distances
M = np.loadtxt('matrix.txt')
G = nx.from_numpy_matrix(M)

np.random.seed(int(time.time()))

C = np.random.rand(22,22)

C = (C+C.T)/2.0

#condutivity

#distances^-1

#print(M)
M[M!=0] = 1/M[M!=0]
#print(M)

#condutivity over distances



D = np.zeros((22,22))

D = np.copy(C)

#print(D.shape[0])


start = time.time()


#testing for the distances matrix in line 38-40
#tested at 19:10
#went right
#
#exit()


V = np.zeros(22)
V[source] = -1
V[sink] = 1

firstout = list()
firstin = list()
x = list()

Q = np.zeros((22,22))
for loop in range(1000):
	#print(D)
	S = np.copy(D)
	#print(S)
	S = S * M
	#print(S)
	
	soma = np.sum(S,axis=0)

	for i in range(S.shape[0]):
		S[i,i] = S[i,i] - soma[i]

	#print("after subtracting:\n",S)

	try:
		P1 = np.linalg.solve(S,V)
	except:
		print(loop)

	P1 = P1 - P1[sink]

	for i in range(Q.shape[0]):
		for j in range(Q.shape[0]):
			Q[i,j] = D[i,j] * (P1[i]-P1[j]) * M[i,j]


	firstout.append(Q[5,0])
	firstin.append(Q[6,0])
	x.append(loop)

	D = systemDynamics(Q,D)
	


	if(False):
		print('\nflux:\n',Q)
		print('\nconductivity:\n',D)
		print('\npressures:\n',P1)
		graphmatrix = np.round(Q,decimals=5)
		graphmatrix = abs(graphmatrix)
		G = nx.from_numpy_matrix(graphmatrix)

		edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())
		pressurelabels = dict(zip(G.nodes() , np.round(P1,decimals=1)))
		nx.draw_networkx(G, pos=positions,with_labels=False,node_size=400,linewidths=0, edgelist=edges, edge_color=weights,edge_cmap=plt.cm.Reds)
		nx.draw_networkx_labels(G,pos=positions,font_size=10,labels=pressurelabels)
		#edge_labels = nx.get_edge_attributes(G,'weight')
		#nx.draw_networkx_edge_labels(G,pos=positions,font_size=10,edge_labels=edge_labels)
		plt.show()

		#input("Press Enter to continue...")


print(Q)

plt.plot(x,firstout,label="externo")
plt.plot(x,firstin,label="interno")
plt.legend()
plt.show()

end = time.time()
print("time elapsed: ",end - start,"\n\n")

graphmatrix = np.round(Q,decimals=5)
graphmatrix = abs(graphmatrix)

G = nx.from_numpy_matrix(graphmatrix)

edge_labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, pos=positions)
nx.draw_networkx_edge_labels(G,pos=positions,font_size=8,edge_labels=edge_labels)
plt.show()






