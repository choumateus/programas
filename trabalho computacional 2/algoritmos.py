import matplotlib.pyplot as plt
import copy
import time

#funcao que monta a matriz no formato COO
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

#funcao que monta o vetor b, dado a matriz
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
#norma para testar a convergência
def norma(x,x0):
    d_maior=abs(x[0]-x0[0])
    for i in range(1,len(x)):
        if abs(x[i]-x0[i])>d_maior:
            d_maior = abs(x[i]-x0[i])
    return d_maior
#retorna o elemento da diagonal, pois ele é preciso no algoritmo
def elem_diagonal(lin,col,val,id):
    for i in range(len(lin)):
        if lin[i] == id and col[i] == id:
            return val[i]

#funcao principal, que faz o algoritmo funcionar
def SOR(lin,col,val, x0, b, tol, max_iter, w):
    k=0
    n = len(b)
    x =copy.copy(x0)

    while k <max_iter:
        for i in range(n):
            soma1=0
            soma2=0
            for j in range(lin.index(i),lin.index(i)+lin.count(i)-1):           #soma valores novos
                if lin[j] > col[j]:
                    soma1+=val[j] * x[col[j]]
            for j in range(lin.index(i)+lin.count(i)-1,lin.index(i),-1):        #soma valores velhos
                if lin[j]<col[j]:
                    soma2+= val[j] * x0[col[j]]
            soma3 = (b[i] - (soma1 + soma2)) / (elem_diagonal(lin,col,val,i))
            soma4 = (1-w)*x0[i]
            x[i] = w*soma3 + soma4
        if norma(x,x0) < tol:
            print("X =", x)
            return k
        x0 = copy.copy(x)
        k+=1
    print("excede 1000 iterações")
    return k

#montando todas as variáveis para a implementacao
linhas=[]
colunas=[]
valores=[]
arquivo = input("entre com o nome do arquivo")
adiciona_elem(str(arquivo),linhas,colunas,valores)
b=vetor_b(linhas,valores)
x0=[0. for i in range(len(b))]
n=1000
TOL = 0.00001
w = float(input("entre com o omega"))
tempo1 = time.time()
print(SOR(linhas,colunas,valores,x0,b,TOL,n,w))
print("tempo: ", time.time() - tempo1)
input()
#cada lista significa um criterio de convergencia, e vai armazenar a quantidade de iteracoes pra cada omega
iteracoes3=[]
iteracoes4=[]
iteracoes2=[]
iteracoes5=[]
iteracoes6=[]

#algoritmo em acao e cronometrando o tempo que ele demora
#import time
tempo1 = time.time()
TOL = 0.01
w = 1
for i in range(99):
    iteracoes2.append(SOR(linhas,colunas,valores,x0,b,TOL,n,w))
    w+=0.01
TOL = 0.001
w = 1
for i in range(99):
    iteracoes3.append(SOR(linhas,colunas,valores,x0,b,TOL,n,w))
    w+=0.01
TOL = 0.0001
w = 1
for i in range(99):
    iteracoes4.append(SOR(linhas,colunas,valores,x0,b,TOL,n,w))
    w+=0.01
TOL = 0.00001
w = 1
for i in range(99):
    iteracoes5.append(SOR(linhas,colunas,valores,x0,b,TOL,n,w))
    w+=0.01
TOL = 0.000001
w=1
for i in range(99):
    iteracoes6.append(SOR(linhas,colunas,valores,x0,b,TOL,n,w))
    w+=0.01
tempo=time.time()-tempo1
plt.title(arquivo)
print(tempo)

#determinando o omega otimo e plotando um grafico para melhor visualizacao
min=iteracoes2[0]
minindex=0
for i in range(len(iteracoes2)):
    if iteracoes2[i] <min:
        min=iteracoes2[i]
        minindex= i
if minindex//10 == 0:
    plt.plot(iteracoes2, label='10e-2 w otimo = 1.0' + str(minindex))
else:
    plt.plot(iteracoes2,label = '10e-2 w otimo = 1.'+str(minindex))
print(minindex)
min=iteracoes3[0]
minindex=0
for i in range(len(iteracoes3)):
    if iteracoes3[i] <min:
        min=iteracoes3[i]
        minindex=i
if minindex//10 == 0:
    plt.plot(iteracoes3, label='10e-3 w otimo = 1.0' + str(minindex))
else:
    plt.plot(iteracoes3,label = '10e-3 w otimo = 1.'+str(minindex))
print(minindex)
min=iteracoes4[0]
minindex=0
for i in range(len(iteracoes4)):
    if iteracoes4[i] <min:
        min=iteracoes4[i]
        minindex=i
if minindex//10 == 0:
    plt.plot(iteracoes4, label='10e-4 w otimo = 1.0' + str(minindex))
else:
    plt.plot(iteracoes4,label = '10e-4 w otimo = 1.'+str(minindex))
print(minindex)
min=iteracoes5[0]
minindex=0
for i in range(len(iteracoes5)):
    if iteracoes5[i] <min:
        min=iteracoes5[i]
        minindex=i
if minindex//10 == 0:
    plt.plot(iteracoes5, label='10e-5 w otimo = 1.0' + str(minindex))
else:
    plt.plot(iteracoes5,label = '10e-5 w otimo = 1.'+str(minindex))
print(minindex)
min=iteracoes6[0]
minindex=0
for i in range(len(iteracoes6)):
    if iteracoes6[i] <min:
        min=iteracoes5[i]
        minindex=i
if minindex//10 == 0:
    plt.plot(iteracoes6, label='10e-6 w otimo = 1.0' + str(minindex))
else:
    plt.plot(iteracoes6,label = '10e-6 w otimo = 1.'+str(minindex))
print(minindex)


plt.xlabel("w = 1._ ")
plt.ylabel("iteracoes")
plt.legend()
plt.show()

import numpy as np

#funcao que multiplica a matriz no formato coo por um vetor
def mult_mat_vet(lin,col,val,vet):
    y = [0. for i in range(len(vet))]
    for i in range(len(lin)):
        y[lin[i]]+=val[i]*vet[col[i]]
    return np.array(y)

#funcao principal do algoritmo do gradiente conjugado
def conjugate_grad(lin,col,val, b, x):
    k=len(b)
    r =b - mult_mat_vet(lin,col,val,x)
    v = r
    i=0
    prod_r = np.dot(r, r)
    #for i in range(k):
    while i < 1000:
        Av = mult_mat_vet(lin,col,val,v)
        t = prod_r / np.dot(v, Av) #To
        x += np.dot(t,v)
        r = b - mult_mat_vet(lin,col,val,x)
        prod_r1 = np.dot(r, r)
        s = prod_r1 / prod_r
        prod_r = prod_r1
        i+=1
        if prod_r1 < 1e-5:
            print('Iterações:', i)
            break
        v = s * v + r
    print('Iterações:', i)
    return x


linhas=[]
colunas=[]
valores=[]
matriz=str(input("nome do arquivo: "))
adiciona_elem(matriz,linhas,colunas,valores)
b=vetor_b(linhas,valores)
xc = [1 for i in range(len(b))]
x = [0. for i in range(len(b))]
import time
tempo1 = time.time()
#print(conjugate_grad(linhas,colunas,valores,b,x))
sol = conjugate_grad(linhas,colunas,valores,b,x)
print(time.time() - tempo1)
print(sol)
print(norma(sol,xc))

