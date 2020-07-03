import numpy as np

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
def metodo_simetrico_da_potencia(matriz,tol,N):
    k=1
    x = [0. for i in range (len(matriz))]
    x[0]=1
    x = np.dot(x,1/norma_2(x))
    while k <= N:
        y = np.dot(matriz,x)
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
            return u
        k+=1
def adiciona_x(matriz,vetor):
    n=len(matriz)
    for i in range(n):
        matriz[i].append(vetor[i])
    return matriz
    #U eh np.transpose(L)

def mult_mat_numero(val, num):
    val1 = val[:]
    for i in range(len(val)):
        val1[i] = val[i] * num
    return val1
def sub_mat_IQ(matriz,IQ):
    matriz1 = matriz[:]
    for i in range (len(matriz)):
        matriz1[i][i] -= IQ
    return matriz1


def norma_infinita(vetor):
    max = abs((vetor[0]))
    for i in range(1,len(vetor)):
        if abs(vetor[i])>abs(vetor[i-1]):
            max = abs(vetor[i])
    return max
def norma_infinita_p(vetor):
    max = (vetor[0])
    for i in range(1,len(vetor)):
        if abs(vetor[i])>abs(vetor[i-1]):
            max = vetor[i]
    return max

def metodo_inverso_da_potencia(matriz,tol,N):
    x = [1. for i in range(len(matriz))]
    vet = np.dot(matriz,x)
    q = max(vet)
    k=1
    xp = norma_infinita_p(x)
    x = np.dot(x,1/xp)
    matriz_diferenca = sub_mat_IQ(matriz, q)
    while k <= N:
        y = np.linalg.solve(matriz_diferenca,x)
        u = norma_infinita_p(y)
        razao = np.dot(y,1/norma_infinita_p(y))
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

def retorna_matriz(arquivo):
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
    return matriz
def algoritmo_de_QR(A,tol,N):
    n = len(A)
    I = []
    for i in range(n):
        I.append([0. for i in range(n)])
        I[i] = 1
    k = 0
    diag = [0 for i in range(n)]
    err = [1 for i in range(n)]
    while k <= N :
        diag_ant = diag
        q, r = np.linalg.qr(A)
        A = np.dot(r,q)
        I = np.dot(I,q)
        diag = np.diag(A)
        erro = 0
        for i in range(n):
            err[i] = abs(diag[i] - diag_ant[i])
            if err[i] > erro:
                erro = err[i]
        if erro <= tol:
            print(-np.sort(-diag))
            return k
        k += 1
    return "maximo excedido"

import time
while True:
    arq = str(input("entre com o nome do arquivo"))
    matriz = retorna_matriz(arq)
    tempo1 = time.time()
    raio = (metodo_simetrico_da_potencia(matriz,0.0000001,10000))
    tempo = time.time() - tempo1
    raio_real = 8.635910e+02
    print(raio ,"&", raio_real,"&", raio - raio_real,"&",tempo)