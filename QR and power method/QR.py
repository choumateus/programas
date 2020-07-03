import numpy as np



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
def algoritmo_de_QR(A,N,tol):
    #n = scipy.sparse.coo_matrix.get_shape(A)[0]
    #n=tamanho
    n = len(A)
    I = []
    for i in range(n):
        I.append([0. for i in range(n)])
        I[i] = 1
    k = 0
    diag = [0 for i in range(n)]
    err = [1 for i in range(n)]
    erro = 1
    while k <= N :
        diag_ant = diag
        q, r = np.linalg.qr(A)
        A = np.dot(r,q)
        I = np.dot(I,q)
        #print(A)
        #input()
        diag = np.diag(A)
        #print(diag)
        #input()
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

print(algoritmo_de_QR(A,10000,0.000000001))