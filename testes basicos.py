from random import randrange
import math as mt
import numpy
import scipy.stats
import chaospy
#funcao desvio padrao para usarmos a propriedade do erro=DV/raiz de N
print("com geradores pseudo-aleatorios")
def desvio_padrao(x,xm):
    var=0
    for i in range(len(x)):
       var+=(x[i]-xm)**2/(len(x)-1)
    return var**(1/2)
def media(x):
    soma = 0
    for i in range(len(x)):
        soma += x[i]/len(x)
    return soma

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
print(" **********************" )
print("com gerador de numeros quasi-aleatorios")
#queremos a media de uma amostra de n x no qual ela se aproxima do valor da integral
n1=1
soma1=0
erro1 = 5 #qualquer numero maior que 0,01
num = chaospy.Uniform(0,1)
integral_estimada1 = 0
while erro1 >= 0.01:
    x = num.sample(n1)
    soma1=0
    xl=[]
    for i in range(len(x)):
        soma1+= f(x[i])
        xl.append(f(x[i]))
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
print(" ******************** ")
print(" com geradores pseudo-aleatorios")
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
print("tamanho da amostra:", n2)
print("erro do hit-miss= ", erro2)
print(" **********************" )
print("com gerador de numeros quasi-aleatorios")
n2 = 1
integral_estimada2 = 0
erro2 = 5
soma2 = 0
while erro2 >= 0.01:
    x , y = num.sample(n2), num.sample(n2) #numeros entre 0 e 1
    soma2=0
    for i in range(n2):
        if f(x[i]) > y[i]:
            soma2+=1
    integral_estimada2 = soma2/n2
    if n2>50:
        erro2 = desvio_padrao_bernoulli(integral_estimada2)/n2**(1/2)
    n2+=1

print("valor estimado:", integral_estimada2)
print("tamanho da amostra:", n2)
print("erro do hit-miss= ", erro2)
print(" ******************** ")
print(" com geradores pseudo-aleatorios")

#Metodo 3: Importance Sampling
#vamos usar uma funcao g(x) que eh a auxiliar desse metodo, ela vai ser a funcao Beta
def beta():
    return numpy.random.beta(0.8,1.0)
def g(x):
    return scipy.stats.beta.pdf(x,0.8,1.0)
def h(x):
    return f(x)/g(x)
n3=1
soma3=0
erro3 = 5 #qualquer numero maior que 0,01
xl3=[]  #lista para o desvio padrao
integral_estimada3 = 0
while erro3>=0.01:
    x = beta()
    soma3 += h(x)
    xl3.append(h(x))
    integral_estimada3 = soma3 / n3
    if n3>20:
        dv=desvio_padrao(xl3,integral_estimada3)
        erro3 = dv/(n3)**(1/2)
    n3+=1

print("valor estimado:", integral_estimada3)
print("tamanho da amostra:", n3)
print("erro do Importance Sampling pela variancia= ", erro3)
print(" **********************" )
print("com gerador de numeros quasi-aleatorios")
def beta(x):
    return scipy.stats.beta.pdf(x,0.8,1.0)
def g(x):
    return scipy.stats.beta.pdf(x,0.8,1.0)
def h(x):
    return f(x)/g(x)
n3=1
soma3=0
erro3 = 5 #qualquer numero maior que 0,01
xl3=[]  #lista para o desvio padrao
xteste=[]
integral_estimada3 = 0
while erro3>=0.01:
    soma3=0
    xl3=[]
    xk=num.sample(1)
    while 0==g(beta(xk[0])) :  #para evitar uma divisao por 0
        xk = num.sample(1)
    for i in range(n3):
        x1 = beta(xk[0])
        soma+=f(x1)/g(x1)
        xl3.append(f(x1/g(x1)))
    integral_estimada3 = soma3 / n3
    if n3>2:
        dv=desvio_padrao(xl3,integral_estimada3)
        erro3 = dv/(n3)**(1/2)
        print(erro3)
    n3+=1
print("valor estimado:", integral_estimada3)
print("tamanho da amostra:", n3)
print("erro do Importance Sampling pela variancia= ", erro3)
print(" ******************** ")
print(" com geradores pseudo-aleatorios")
#Metodo 4 : funcao auxiliar
#usaremos uma funcao que se comporta de forma similar a nossa f(x)
def t(x):       #esta funcao tem um coeficiente de correlacao perto de 1 com nossa f(x)
    return 1-0.4*x
def cov(a,b):
    soma= 0
    for i in range (len(a)):
        soma += ((a[i]-media(a))*(b[i]-media(b)))/(len(a))
    return soma
def var(x,xm):
    var=0
    for i in range(len(x)):
       var+=(x[i]-xm)**2/(len(x)-1)
    return var
n4=1
somaf=0
somat=0
erro4= 5 #qualquer numero maior que 0,01
fl, tl=[],[] #listas para a variancia e covariancia
integral_estimada4 = 0
c = 0   #a-â
while erro4 >= 0.01:
    x= randrange(0,10000000)/10000000
    somaf+=f(x)
    somat+=t(x)
    fl.append(f(x))
    tl.append(t(x))
    integralf = somaf/n4
    integralt = somat/n4
    c = integralf-integralt
    integral_estimada4 = integralt + c
    if n4 > 2:
        erro4 = ((var(fl,media(fl)) + var(tl,media(tl)) - 2*cov(fl,tl))/n4)**(1/2)
    n4+=1
print("valor estimado:", integral_estimada4)
print("tamanho da amostra:", n4)
print("erro do ultimo metodo pela variancia= ", erro4)
print(" **********************" )
print("com gerador de numeros quasi-aleatorios")
