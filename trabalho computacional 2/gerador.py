import numpy as np
import matplotlib.pyplot as plt
import copy
def adiciona_elem(arquivo,linhas,colunas,valores):
    arq = open(arquivo,"r")
    for i in arq:
        elem = i.split()
        linhas.append(int(elem[1])-1)
        colunas.append(int(elem[0])-1)
        valores.append(float(elem[2]))
def vetor_b(linhas,valores):
    b=[]
    i=0
    soma=0
    while i < len(linhas)-1:
        soma=0
        linha=linhas[i]
        while linha == linhas[i] and i < len(linhas)-1:
            soma+=valores[i]
            i+=1
        b.append(soma)
    if linhas[-1] == linhas[-2]:
        b[-1] += valores[-1]
    if linhas[-1] != linhas[-2]:
        b.append(valores[-1])
    return b

def mult_mat_vet(lin,col,val,vet):
    y = [0. for i in range(len(vet))]
    for i in range(len(lin)):
        y[lin[i]]+=val[i]*vet[col[i]]
    return y
def norma(x,x0):
    d_maior=abs(x[0]-x0[0])
    for i in range(1,len(x)):
        if abs(x[i]-x0[i])>d_maior:
            d_maior = abs(x[i]-x0[i])
    return d_maior

def elem_diagonal(lin,col,val,id):
    for i in range(len(lin)):
        if lin[i] == id and col[i] == id:
            return val[i]

def norma(x,x0):
    d_maior=abs(x[0]-x0[0])
    for i in range(1,len(x)):
        if abs(x[i]-x0[i])>d_maior:
            d_maior = abs(x[i]-x0[i])
    return d_maior

def SOR(lin,col,val, x0, b, tol, max_iter, w):
    k=0
    if (w < 1 or w >= 2):
        print('w deve estar no intervalo [1, 2)')
        x = float('nan')
        print(x)
        return
    n = len(b)
    x =copy.copy(x0)

    while k <max_iter:
        #print(x)
        #input()
        for i in range(n):
            soma1=0
            soma2=0
            for j in range(lin.index(i),lin.index(i)+lin.count(i)-1):
                #print(i)
                #print(j)
                #input("parte 1")
                #input("index j")
                if lin[j] > col[j]:
                    #print(j)
                    soma1+=val[j] * x[col[j]]
                    #print(soma1)
                    #input("somou")
            for j in range(lin.index(i)+lin.count(i)-1,lin.index(i),-1):
                #print(i)
                #print(j)
                #input("parte 2")
                if lin[j]<col[j]:
                    soma2+= val[j] * x0[col[j]]
            #print(elem_diagonal(lin,col,val,i))
            #print(soma1)
            #print(soma2)
            #input()
            soma3 = (b[i] - (soma1 + soma2)) / (elem_diagonal(lin,col,val,i))
            #x[i] = (elem_diagonal(lin,col,val,i))
            soma4 = (1-w)*x0[i]
            x[i] = w*soma3 + soma4
        if norma(x,x0) < tol:
            print(k, "iterações")
            print("X =", x)
            return k
        x0 = copy.copy(x)
        k+=1
    print(k, "iterações")
    print("X =",x)
    return k
linhas=[]
colunas=[]
valores=[]
arquivo = input("entre com o nome do arquivo")
adiciona_elem(str(arquivo),linhas,colunas,valores)
#b=[24,30,-24]
b=vetor_b(linhas,valores)
x0=[0. for i in range(len(b))]
print(linhas)
print(valores)
print()
print(b)
n=1000
TOL = 0.001
iteracoes1=[]
iteracoes3=[]
iteracoes4=[]
iteracoes2=[]
iteracoes5=[]
iteracoes6=[]
w=1.03
print(SOR(linhas,colunas,valores,x0,b,TOL,n,w))