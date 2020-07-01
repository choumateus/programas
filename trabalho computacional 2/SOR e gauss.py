import numpy as np
import matplotlib.pyplot as plt
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
            matriz[int(elem[1])-1][int(elem[0])-1] = float(elem[2])
    return matriz

def vetor_b(matriz):
    b=[]
    for i in matriz:
        b.append(sum(i))
    return b

def norma(x,x0):
    d_maior=abs(x[0]-x0[0])
    for i in range(1,len(x)):
        if abs(x[i]-x0[i])>d_maior:
            d_maior = abs(x[i]-x0[i])
    return d_maior

def SOR(matriz, b, n, TOL, w): # n = maximo de interacoes, TOL = criterio de parada
    k=1
    vetor_sol0 = [0 for i in range (len(b))]
    vetor_sol = [0 for i in range(len(b))]
    while k <= n:
        print(vetor_sol)
        input()
        for i in range(len(matriz)):
            soma1 = 0
            soma2 = 0
            for j in range(i):
                print(soma1)
                #input("somou")
                soma1 += matriz[i][j] * vetor_sol[j]
            for j in range(i+1,len(matriz)):
                print(soma2)
                soma2 += matriz[i][j] * vetor_sol0[j]
            soma3 = b[i] - soma1 - soma2
            soma4 =(1-w)*vetor_sol0[i]
            vetor_sol[i] =soma4 + (w*soma3)/matriz[i][i]
        #print(vetor_sol)
        if norma(vetor_sol,vetor_sol0)<TOL:
            #print(vetor_sol)
            print(k)
            return k
        k+=1
        for i in range(len(vetor_sol)):
            vetor_sol0[i] = vetor_sol[i]
    return "depois de ",  n ," iteracoes, o sistema nao convergiu"
matrizdesejada=input("entre com a matriztxt desejada: ")
#a=le_matriz(str(matrizdesejada))
#print(np.array(a))
#b=vetor_b(a)
n=100000
TOL = 0.000001
w=1.2
iteracoes1=[]
iteracoes2=[]
iteracoes3=[]
iteracoes4=[]
iteracoes5=[]
iteracoes6=[]
#a=[[3.0, 1.0, 0., 0., 0., 0., 0., 0., 0., 0.],[1.0, 3.0, 1.0, 0., 0., 0., 0., 0., 0., 0.], [0., 1.0, 3.0, 1.0, 0., 0., 0., 0., 0., 0.], [0., 0, 1.0, 3.0, 1.0, 0., 0., 0., 0., 0.], [0., 0., 0., 1.0, 3.0, 1.0, 0., 0., 0., 0.], [0., 0., 0., 0., 1.0, 3.0, 1.0, 0., 0., 0.], [0., 0., 0., 0., 0., 1.0, 3.0, 1.0, 0., 0.], [0., 0., 0., 0., 0., 0., 1.0, 3.0, 1.0, 0.], [0., 0., 0., 0., 0., 0., 0., 1.0, 3.0, 1.0], [0., 0., 0., 0., 0., 0., 0., 0., 1.0, 3.0]]
a=[[4,3,0],[3,4,-1],[0,-1,4]]
b=[24,30,-24]
print(SOR(a,b,n,TOL,1.25))
input("PAAAAAAAAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRRRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")