import numpy as np
import math

x = np.array([[3.0, 1.0, 0., 0., 0., 0., 0., 0., 0., 0.],[1.0, 3.0, 1.0, 0., 0., 0., 0., 0., 0., 0.], [0., 1.0, 3.0, 1.0, 0., 0., 0., 0., 0., 0.], [0., 0, 1.0, 3.0, 1.0, 0., 0., 0., 0., 0.], [0., 0., 0., 1.0, 3.0, 1.0, 0., 0., 0., 0.], [0., 0., 0., 0., 1.0, 3.0, 1.0, 0., 0., 0.], [0., 0., 0., 0., 0., 1.0, 3.0, 1.0, 0., 0.], [0., 0., 0., 0., 0., 0., 1.0, 3.0, 1.0, 0.], [0., 0., 0., 0., 0., 0., 0., 1.0, 3.0, 1.0], [0., 0., 0., 0., 0., 0., 0., 0., 1.0, 3.0]])
b = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
x0 = np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,0,0,0,0])
tol =  10 ** (-15)
max_iter = 20
w = 1
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
            matriz[int(elem[0])-1][int(elem[1])-1] = float(elem[2])
    return matriz

def vetor_b(matriz):
    b=[]
    for i in matriz:
        b.append(sum(i))
    return b
def SOR(A, b, x0, tol, max_iter, w):
    if (w<=1 or w>2):
        print('w should be inside [1, 2)');
        step = -1;
        x = float('nan')
        return
    n = b.shape
    x = x0

    for step in range (1, max_iter):
        for i in range(n[0]):
            new_values_sum = np.dot(A[i, 1 : (i - 1)], x[1 : (i - 1)])
            for j in range(i + 1, n[0]):
                old_values_sum = np.dot(A[i, j], x0[j])
            x[i] = b[i] - (old_values_sum + new_values_sum) / A[i, i]
            x[i] = np.dot(x[i], w) + np.dot(x0[i], (1 - w))

        if (np.linalg.norm(x - x0) < tol):
            print(step)
            break
        x0 = x


    print("X = {}".format(x))
    print("The number of iterations is: {}".format(step))
x=le_matriz("matriz1")
b=vetor_b(x)

SOR(x, b, x0, tol, max_iter, w)