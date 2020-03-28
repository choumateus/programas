from random import randrange
import math as mt
import numpy
import scipy.stats
#funcao desvio padrao para usarmos a propriedade do erro=DV/raiz de N
def desvio_padrao(x,xm):
    var=0
    for i in range(len(x)):
       var+=(x[i]-xm)**2/(len(x)-1)
    return var**(1/2)

#vamos montar a funcao dada do enunciado
b=0.11221352     #NUSP
a=0.501925028  #RG
def f(x):
    return mt.e**(-a*x)*mt.cos(b*x)

#Metodo 1: Crude Monte Carlo
#queremos a media de uma amostra de n x no qual ela se aproxima do valor da integral
n1=1
soma1=0
erro1 = 5 #qualquer numero maior que 0,01
xl=[]  #lista para o desvio padrao
integral_estimada1 = 0
while erro1 >= 0.01:
    x=randrange(0,10000000)/10000000
    soma1 += f(x)
    xl.append(f(x))
    integral_estimada1 = soma1/n1
    if n1<5:
        n1+=1
    else:
        dv=desvio_padrao(xl,integral_estimada1)
        erro1 = dv/(n1)**(1/2)
        n1+=1
print("valor estimado:", integral_estimada1)
print("tamanho da amostra:", n1)
print("erro do Crude pela variancia= ", erro1)

#Metodo 2: hit-miss
#pegamos coordenadas aleatorias,caso ela esteja "dentro da curva"contamos
#sabemos atraves de uma analise de grafico que a funcao f entre 0 e 1 possui um valor maximo de um
#definimos a funcao desvio padrao para uma bernoulli, ja que se trata dessa distribuicao
def desvio_padrao_bernoulli(p):
    return (p*(1-p))**(1/2)
n2 = 1
integral_estimada2 = 0
erro2 = 5
soma = 0
while erro2 >= 0.01:
    x , y = randrange(0,10000000)/10000000 , randrange(0,10000000)/10000000 #numeros entre 0 e 1
    if f(x) > y:
        soma+=1
    integral_estimada2 = soma/n2
    if n2>50:
        erro2 = desvio_padrao_bernoulli(integral_estimada2)/n2**(1/2)
    n2+=1

print("valor estimado:", integral_estimada2)
print("tamanho da amostra:", n2-1)
print("erro do hit-miss= ", erro2)

#Metodo 3: Importance Sampling
#vamos usar uma funcao g(x) que eh a auxiliar desse metodo, ela vai ser a funcao Beta
def beta():
    return numpy.random.beta(0.96,1.02)
def g(x):
    return scipy.stats.beta.pdf(x,0.96,1.02)
def h(x):
    return f(x)/g(x)
n3=1
soma3=0
erro3 = 5 #qualquer numero maior que 0,01
xl3=[]  #lista para o desvio padrao
integral_estimada3 = 0
while erro3>=0.01:
    if n3<20:
        x = beta()
        if g(x)>=f(x):
            val =h(x)
            soma3 += val
            xl3.append(val)
            integral_estimada3 = soma3 / n3
            n3+=1
    else:
        x = beta()
        if g(x)>=f(x):
            soma3 += h(x)
            xl3.append(h(x))
            integral_estimada3 = soma3 / n3
            dv=desvio_padrao(xl3,integral_estimada3)
            erro3 = dv/(n3)**(1/2)
            n3+=1

print("valor estimado:", integral_estimada3)
print("tamanho da amostra:", n3)
print("erro do Importance Sampling pela variancia= ", erro3)



