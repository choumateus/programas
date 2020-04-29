def gerador(n):
    mat=[[0 for i in range(n+1)]for j in range(n)]
    n = len(mat)
    for i in range(n):
        for j in range(n):
            mat[i][j] = 1/(i+j+1) #somamos 1 , pois o index do python comeca do 0 e nao do 1, logo temos ((i+1)+(j+1)-1)
    for i in range(n):            #que é igual a i+j+1
        for j in range(n):
            mat[i][-1]+=mat[i][j]
    return mat
a=gerador(4)
b=gerador(4)
def sem_pivo(n):
    Matriz= gerador(n)
    n = len(Matriz)
    if len(Matriz) != len(Matriz[0])-1:
        return "sem solucao"
    for i in range(0, n):
        #escalonando a matriz
        for k in range(i + 1, n):
            c = Matriz[k][i] / Matriz[i][i]
            for j in range(i, n + 1):
                Matriz[k][j] -= c * Matriz[i][j]

    # monta e soluciona a equacao, com a matriz triangular
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        try:
            x[i] = Matriz[i][n] / Matriz[i][i]
        except:
            return "sem solucao unica" #caso de divisao por 0
        for k in range(i - 1, -1, -1):
            Matriz[k][n] -= Matriz[k][i] * x[i]
    return x
def pivotamento_parcial(n):
    Matriz = gerador(n)
    if len(Matriz) != len(Matriz[0]) - 1:
        return "sem solucao"
    n = len(Matriz)

    # encontrando o maior elemento da coluna para realizar a troca
    for i in range(0, n):
        maxEl = Matriz[i][i]
        maxRow = i
        for k in range(i + 1, n):
            if Matriz[k][i] > maxEl:
                maxEl = Matriz[k][i]
                maxRow = k

        if i!=maxRow:
            Matriz[maxRow], Matriz[i] = Matriz[i] , Matriz[maxRow]

        # escalonando a matriz#
        for k in range(i + 1, n):
            c = Matriz[k][i] / Matriz[i][i]
            for j in range(i, n + 1):
                Matriz[k][j] -= c * Matriz[i][j]

        # monta e soluciona a equacao, com a matriz triangular
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        try:
            x[i] = Matriz[i][n] / Matriz[i][i]
        except:
            return "sem solucao unica" #caso de divisao por 0
        for k in range(i - 1, -1, -1):
            Matriz[k][n] -= Matriz[k][i] * x[i]
    return x
def norma_2(x):
    soma=0
    for i in range(len(x)):
        soma+= (x[i]-1)**2
    return (soma)**(1/2)
def determinante(Matriz):
    n = len(Matriz)
    deter=1
    for i in range(0, n):
        #escalonando a matriz
        for k in range(i + 1, n):
            c = Matriz[k][i] / Matriz[i][i]
            for j in range(i, n):
                Matriz[k][j] -= c * Matriz[i][j]
    for i in range(n):
        deter*=Matriz[i][i]
    return(deter)
print("*************             PARTE 1               ****************" )
rodar = "sim"
n=2
while rodar != "nao":
    print("solucao encontrada pelo algoritmo sem pivo: ",sem_pivo(n))
    print()
    print("norma 2 do vetor x da solucao sem pivo com o a solucao oficial", norma_2(sem_pivo(n)))
    print()
    print("determinante da matriz de hilbert", determinante(gerador(n)))
    print()
    print("solucao encontrada pelo algoritmo com pivotamento parcial: ", pivotamento_parcial(n))
    print()
    print("norma 2 do vetor x da solucao com pivotamento parcial com o a solucao oficial", norma_2(pivotamento_parcial(n)))
    print()
    rodar = input("continuo rodando essa parte? (sim ou nao) ")
    if rodar != "nao":
        x = int(input("em quantas unidades voce deseja aumentar o n? "))
        n+=x
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
    #U eh np.transpose(L)
def resolve_chulesky(L,U,Y):
    n= len(L)
    MatrizU = [[] for i in range(n)]
    #juntando numa matrizU para resolver o sistema
    for i in range(n):
        for j in range(n):
            MatrizU[i].append(U[i][j])
        MatrizU[i].append(Y[i])
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
def sem_pivo_2(Matriz1):
    n = len(Matriz1)
    Matriz=[[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            Matriz[i].append(Matriz1[i][j])
    adiciona_y(Matriz)
    if len(Matriz) != len(Matriz[0])-1:
        return "sem solucao"
    for i in range(0, n):
        #escalonando a matriz
        for k in range(i + 1, n):
            c = Matriz[k][i] / Matriz[i][i]
            for j in range(i, n + 1):
                Matriz[k][j] -= c * Matriz[i][j]

    # monta e soluciona a equacao, com a matriz triangular
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        try:
            x[i] = Matriz[i][n] / Matriz[i][i]
        except:
            return "sem solucao unica" #caso de divisao por 0
        for k in range(i - 1, -1, -1):
            Matriz[k][n] -= Matriz[k][i] * x[i]
    return x
import time
print("***********      PARTE 2         *************")
rodar2="sim"
n=2
while rodar2!= "nao":
    a = matriz_randomica(n)
    y = cria_vetor_y(a)
    l = cholesky(a)
    u = np.transpose(l)
    tempo1=time.time()
    print("solucao encontrada pelo algoritmo de chulesky:", resolve_chulesky(u,l,y))
    print()
    tempo2=time.time()
    print("tempo computacional: " , tempo2-tempo1)
    print()
    print("norma 2 encontrada pelo algoritmo de chulesky: ", norma_2(resolve_chulesky(u,l,y)))
    print()
    tempo1=time.time()
    print("solucao encontrada pelo algoritmo sem pivo: ",sem_pivo_2(a))
    print()
    tempo2=time.time()
    print("tempo computacional: " , tempo2-tempo1)
    print()
    print("norma 2 encontrada pelo algoritmo sem pivo: ",norma_2(sem_pivo_2(a)))
    print()
    tempo1=time.time()
    print("solucao encontrada pelo algoritmo pronto do numpy: ", np.linalg.solve(a,y))
    print()
    tempo2=time.time()
    print("tempo computacional: " , tempo2-tempo1)
    print()
    print("norma 2 encontrada pelo algoritmo pronto do numpy: ", norma_2(np.linalg.solve(a,y)))
    print()
    print("determinante da matriz: ", determinante(a))
    print()
    rodar2 = input("continuo rodando essa parte? (sim ou nao) ")
    if rodar2 != "nao":
        x = int(input("em quantas unidades voce deseja aumentar o n? "))
        n+=x