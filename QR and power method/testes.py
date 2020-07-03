import numpy as np
from math import sqrt
def adiciona_elem_nao_sim(arquivo, linha, coluna, valor):
    arq = open(arquivo, "r")
    n = "primeiro"
    matriz = []
    for i in arq:
        elem = i.split()
        if n == "primeiro":
            matriz = [[0 for i in range(int(elem[0]))] for j in range(int(elem[1]))]
            n = "não"
        else:
            matriz[int(elem[0]) - 1][int(elem[1]) - 1] = float(elem[2])
            #matriz[int(elem[1]) - 1][int(elem[0]) - 1] = float(elem[2])
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != 0:
                linha.append(i)
                coluna.append(j)
                valor.append(matriz[i][j])
def adiciona_elem(arquivo, linha, coluna, valor):
    arq = open(arquivo, "r")
    n = "primeiro"
    matriz = []
    for i in arq:
        elem = i.split()
        if n == "primeiro":
            matriz = [[0 for i in range(int(elem[0]))] for j in range(int(elem[1]))]
            n = "não"
        else:
            matriz[int(elem[0]) - 1][int(elem[1]) - 1] = float(elem[2])
            matriz[int(elem[1]) - 1][int(elem[0]) - 1] = float(elem[2])
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != 0:
                linha.append(i)
                coluna.append(j)
                valor.append(matriz[i][j])

def mult_mat_vet(lin,col,val,vet):
    y = [0. for i in range(len(vet))]
    for i in range(len(lin)):
        y[lin[i]]+=val[i]*vet[col[i]]
    return y
def norma_2(vet):
    soma = 0
    for i in vet:
        soma+=i**2
    return soma**(1/2)
def metodo_simetrico_da_potencia(lin,col,val,tol,N):
    k=1
    x = [0. for i in range (lin[-1]+1)]
    x[0]=1
    x = np.dot(x,1/norma_2(x))
    while k <= N:
        y = mult_mat_vet(lin,col,val,x)
        u = np.dot(x,y)
        if norma_2(y) == 0 :
            return "X invalido"
        razao = np.dot(y,1/norma_2(y))
        diferenca = []
        for i in range(len(x)):
            diferenca.append(x[i] - razao[i])
        erro = norma_2(diferenca)
        x = np.dot(y,1/norma_2(y))
        if erro < tol:
            print(k)
            return u,x
        k+=1
def adiciona_x(matriz,vetor):
    n=len(matriz)
    for i in range(n):
        matriz[i].append(vetor[i])
    return matriz
    #U eh np.transpose(L)
def sem_pivo_2(Matriz1,vetor):
    n = len(Matriz1)
    Matriz=[[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            Matriz[i].append(Matriz1[i][j])
    adiciona_x(Matriz,vetor)
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
def mult_mat_numero(val, num):
    val1 = val[:]
    for i in range(len(val)):
        val1[i] = val[i] * num
    return val1
def sub_mat_IQ(lin1,col1,val1,IQ):
    val=val1[:]
    for i in range(len(lin1)):
        if lin1[i] == col1[i]:
            val[i] = val1[i] - IQ
    return val

def norma_infinita(vetor):
    max = vetor[0]
    for i in range(1,len(vetor)):
        if abs(vetor[i])>abs(vetor[i-1]):
            max = abs(vetor[i])
    return max

def metodo_inverso_da_potencia(lin,col,val,tol,N):
    x = [1. for i in range (lin[-1]+1)]
    xA = mult_mat_vet(lin,col,val,x)
    xAx = np.dot(xA,x)
    xx = np.dot(x,x)
    q = xAx/xx
    k=1
    xp = norma_infinita(x)
    x = np.dot(x,1/xp)
    while k <= N:
        val_diferenca = sub_mat_IQ(lin,col,val,q)
        matriz_normal = COO_para_tradicional(lin,col,val_diferenca)
        y = sem_pivo_2(matriz_normal,x)
        u = norma_infinita(y)
        razao = np.dot(y,1/norma_infinita(y))
        diferenca = []
        for i in range(len(razao)):
            diferenca.append(x[i]-razao[i])
        erro = norma_infinita(diferenca)
        x = np.dot(y,1/norma_infinita(y))
        if erro < tol:
            u = (1/u) + q
            print(k)
            return(u,x)
        k+=1
    return "maximo excedido"
def COO_para_tradicional(lin,col,val):
    matriz = [[0. for i in range(lin[-1]+1)]for i in range(lin[-1]+1)]
    for i in range(len(lin)):
        matriz[lin[i]][col[i]] = val[i]
    return matriz

linhas = []
colunas = []
valores = []
matriz = str(input("entre com o nome do arquivo"))
adiciona_elem(matriz,linhas,colunas,valores)
print(metodo_simetrico_da_potencia(linhas,colunas,valores,0.0001,1000))