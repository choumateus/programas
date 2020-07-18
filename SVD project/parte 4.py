import numpy as np
def latex(matriz):
    for i in range (len(matriz)):
        if len(matriz[0]) == 4:
            print(matriz[i][0],"&",matriz[i][1],"&",matriz[i][2],"&",matriz[i][3],"\\"+"\\")
        if len(matriz[0])==5:
            print(matriz[i][0], "&", matriz[i][1], "&", matriz[i][2],"&",matriz[i][3],"&",matriz[i][4],"\\"+"\\")
A = [[
1 ,0, 0, 0],
[1, 0.25, 0.0625, 0.25**3],
[1 ,0.5, 0.25, 0.5**3],
[1, 0.75, 0.5625, 0.75**3]
,[1,1 ,1,1]]
b = [1.0000,
1.2840,
1.6487,
2.1170,
2.7183]
U, s1,Vt =np.linalg.svd(A)
s=[]
for i in range(len(s1)):
    s.append(s1[i])
S = [[0 for i in range(len(A[0]))] for i in range(len(A))]
for i in range(len(s)):
    S[i][i] = s[i]
latex(A)
input("U,S,V")
latex(U)
input()
latex(S)
latex(Vt)

Ut = np.transpose(U)
c = np.dot(Ut,b)
print("c =", c)
z = []
for i in range(4):
    z.append(c[i]/S[i][i])
print("z =",z)
V = np.transpose(Vt)
latex(V)
x = np.dot(V,z)
print("x =", x)
print("comando pronto no numpy minimoms quadrados = ", np.linalg.lstsq(A,b,rcond=None)[0])