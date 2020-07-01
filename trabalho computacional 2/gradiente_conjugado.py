import numpy as np

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

def adiciona_elem(arquivo,linha,coluna,valor):
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
            matriz[int(elem[1])-1][int(elem[0])-1] = float(elem[2])
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
    return np.array(y)

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
def norma(x,x0):
    d_maior=abs(x[0]-x0[0])
    for i in range(1,len(x)):
        if abs(x[i]-x0[i])>d_maior:
            d_maior = abs(x[i]-x0[i])
    return d_maior

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