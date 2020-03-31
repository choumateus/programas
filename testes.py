import math as mt
import random
def media(x):
    soma = 0
    for i in range(len(x)):
        soma += x[i]/len(x)
    return soma
def correl(a,b):
    nom = 0
    dem1 = 0
    dem2 = 0
    for i in range (len(a)):
        nom += (a[i]-media(a))*(b[i]-media(b))
        dem1 += (a[i] - media(a))**2
        dem2 += (b[i] - media(b))**2
    dem = (dem1*dem2)**(1/2)
    return nom/dem

b=0.11221352     #NUSP
a=0.501925028  #RG
def f(x):
    return mt.e**(-a*x)*mt.cos(b*x)
def g(x):
    return 1-0.4*x
fl = []
gl = []

for i in range(1000):
    x = random.randrange(0,100000)/100000
    fl.append(f(x))
    gl.append(g(x))
print(correl(fl,gl))
