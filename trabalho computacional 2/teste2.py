import numpy as np
import math
import copy
def le_matriz(arquivo):
    arq = open(arquivo,"r")
    n="primeiro"
    matriz=[]
    for i in arq:
        elem = i.split()
        if n == "primeiro":
            matriz=[[0 for i in range(int(elem[0]))]for j in range(int(elem[1]))]
            n = "não"
        else:
            matriz[int(elem[0])-1][int(elem[1])-1] = float(elem[2])#+0.0
    return matriz

def vetor_b(matriz):
    b=[]
    for i in matriz:
        b.append(sum(i))
    return b
A=np.array(le_matriz(str(input("aqruivo"))))
#A = np.array([[4.0,3.0,0.0],[3.0,4.0,-1.0],[0.0,-1.0,4.0]])
#b = np.array([24.,30.,-24.])
b = np.array(vetor_b(A))
x0 = np.array([0. for i in range(len(A))])
tol =  10 ** (-5)
max_iter = 2000
w = 1.72

def SOR(A, x0, b, tol, max_iter, w):
    if (w < 1 or w >= 2):
        print('w deve estar no intervalo [1, 2)')
        step = -1
        x = float('nan')
        print(x)
        return
    n = len(b)
    x =copy.copy(x0)

    for step in range (1, max_iter):
        for i in range(n):
            new_values_sum = np.dot(A[i, :i], x[:i])
            #print(A[i, :i], x[:i])
            old_values_sum = np.dot(A[i, i+1 :], x0[ i+1: ])
            #print(A[i, i+1 :], x0[ i+1: ])
            #input()
            x[i] = (b[i] - (old_values_sum + new_values_sum)) / A[i, i]
            x[i] = np.dot(x[i], w) + np.dot(x0[i], (1 - w))

        if (np.linalg.norm(np.dot(A, x)-b, np.inf) < tol):
            print(step)
            break
        x0 = copy.copy(x)

    print("Há {} iterações".format(step))
    print("X = {}".format(x))
    return step
x = SOR(A, x0, b, tol, max_iter, w)
print()
print("Ax = b")
print(np.dot(A, x))
cont =[]
w=1
min=0
for i in range(99):
    w+=0.01
    cont.append(SOR(A,x0,b,tol,max_iter,w))
    if cont[i]<cont[min]:
        min = i
import matplotlib.pyplot as plt
plt.plot(cont)
plt.show()
print(min)