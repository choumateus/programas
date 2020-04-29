def resolve_chulesky(L,U,Y):
    n= len(L)
    MatrizU = [[] for i in range(n)]
    #juntando numa matrizU para resolver o sistema
    for i in range(n):
        for j in range(n):
            MatrizU[i].append(U[i][j])
        MatrizU[i].append(Y[i])
    print(MatrizU)
    y = [0 for i in range(n)]
    for i in range(n ):
        try:
            y[i] = MatrizU[i][n] / MatrizU[i][i]
        except:
            return "sem solucao unica" #caso de divisao por 0
        for k in range(i ,n):
            MatrizU[k][n] -= MatrizU[k][i] * y[i]
    MatrizL = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            MatrizL[i].append(L[i][j])
        MatrizL[i].append(y[i])
    print(MatrizL)
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        try:
            x[i] = MatrizL[i][n] / MatrizL[i][i]
        except:
            #print("oi")
            return "sem solucao unica" #caso de divisao por 0
        for k in range(i - 1, -1, -1):
            MatrizL[k][n] -= MatrizL[k][i] * x[i]
    return x
import random
import numpy as np
def matriz_randomica(n):
    matriz =[[random.random() for i in range(n)] for i in range(n)]
    matriz1 = np.transpose(matriz)
    matriz2 = np.dot(matriz,matriz1)
    return matriz2
def adiciona_y(matriz):
    n=len(matriz)
    for i in range(n):
        soma=0
        for j in range(n):
            soma+=matriz[i][j]
        matriz[i].append(soma)
    return matriz
def cria_vetor_y(matriz):
    n=len(matriz)
    v=[]
    for i in range(n):
        soma=0
        for j in range(n):
            soma+=matriz[i][j]
        v.append(soma)
    return v
from math import sqrt
def cholesky(A):
    n = len(A)

    # criando a matriz L
    L = [[0.0] * n for i in range(n)]

    for i in range(n):
        for k in range(i + 1):
            somatorio = sum(L[i][j] * L[k][j] for j in range(k))

            if (i == k):  # elementos da diagonal
                L[i][k] = sqrt(A[i][i] - somatorio)
            else:           #elementos fora da diagonal
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - somatorio))
    return L
a=matriz_randomica(16)
y=cria_vetor_y(a)

l=cholesky(a)

print(resolve_chulesky(np.transpose(l),l,y))
