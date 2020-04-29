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
a=matriz_randomica(4)
print(a)
#adiciona_y(a)
b=cria_vetor_y(a)
#print(adiciona_y(a))
#b=np.array(a)
#c=[[3,1], [1,2]]
#d=[9,8]
print(np.linalg.solve(a,b))