from random import randrange
import math as mt
#primeiro vamos estimar um valor muito proximo do valor da intergral que queremos calcular
#para isso vamos simular varias vezes monte carlo e achar a media de todas as simulacoes
b=0.11221352      #NUSP
a=0.501925028  #RG
MC = [] #lista com os resultados das simulacoes
N = 200 #vamos simular 100 vezes
n = 10000 #vamos ter 10000 numeros aleatorios entre 0 e 1 para x
integral = 0
def f(x):
    return mt.e**(-a*x)*mt.cos(b*x)
for i in range(N):
    soma = 0
    for j in range(n):
        x=randrange(0,10000000)/10000000 #numero aleatorio entre 0 e 1
        soma+=f(x)
    MC.append(soma/n)#uma integral encontrada
for j in MC:
    integral+=j/N #media das integrais

#Metodo Crude Monte Carlo
#queremos a media de uma amostra de n x no qual ela se aproxima do valor da integral
n1=1
integral_estimada1=0
erro1 = 5 #qualquer numero maior que 0,01
while erro1 >= 0.01:
    integral_estimada1 = 0
    for i in range(n):
        x=randrange(0,10000000)/10000000
        integral_estimada1 += f(x)/n
    erro1 = abs(integral_estimada1-integral)/integral
    n+=1
print("valor estimado:", integral_estimada1)
print("tamanho da amostra:", n1)
print("erro do Crude= ", erro1)

#Metodo hit-miss
#pegamos coordenadas aleatorias,caso ela esteja "dentro da curva"contamos
#primeiro precisamos estimar o ponto maximo, para obtermos o "retangulo" dos numeros aleatorios
maxy = 0
for i in range(1000):
    x = i/1000
    print(f(x))
    if f(x) > maxy:
        maxy = f(x)
        print(maxy)
x , y = randrange(0,1) , randrange(0,1)
