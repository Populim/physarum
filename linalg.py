import numpy as np
import matplotlib.pyplot as plt

size = 22
zero = 4
X = np.random.rand(size)
X[zero] = 0
print(X)

A = np.random.rand(size,size)
A = (A+A.T)/2.0
A = A*0.01

B = np.dot(A,X)

#print("A: ")
#print(A)
print("X: ")
print(X)
print("B: ")
print(B)

Y = np.linalg.solve(A,B)
Y[Y < 1E-10] = 0
print("Y:")
print(Y)
print(X-Y)


newA = np.delete(A,(zero),axis=0)
newA = np.delete(newA,(zero),axis=1)
newB = np.delete(B,(zero)) 

#print("newA: ")
#print(newA)

newY = np.linalg.solve(newA,newB)
newY[newY < 1E-10] = 0
print("newY:")
print(newY)