import numpy as np
def norma(mat1,mat2):
    norma = 0
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            norma += (mat1[i][j] - mat2[i][j])**2
    return norma**(1/2)
def latex(matriz):
    for i in range (len(matriz)):
        if len(matriz[0]) == 3:
            print(matriz[i][0],"&",matriz[i][1],"&",matriz[i][2],"\\"+"\\")
        if len(matriz[0])==5:
            print(matriz[i][0], "&", matriz[i][1], "&", matriz[i][2],"&",matriz[i][3],"&",matriz[i][4],"\\"+"\\")
A = np.random.rand(5,3)
import time
tempo1 = time.time()
U, s1,Vt =np.linalg.svd(A)
tempo = time.time() - tempo1
s=[]
for i in range(len(s1)):
    s.append(s1[i])
S = [[0 for i in range(len(A[0]))] for i in range(len(A))]
for i in range(len(s)):
    S[i][i] = s[i]
latex(A)
input("U,S,V")
latex(U)
latex(S)
latex(Vt)
input("transposta U e inversa U respectivamente")
latex(np.transpose(U))
input()
latex(np.linalg.inv(U))
input("transposta Vt e inversa Vt")
latex(np.transpose(Vt))
input()
latex(np.linalg.inv(Vt))

us = np.dot(U,S)
P = np.dot(us,Vt)
input("A")
latex(A)
input("P")
latex(P)
print("norma: " ,norma(A,P))
print(tempo)
