from random import randrange
import math as mt
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

#Metodo Crude Monte Carlo
#queremos a media de uma amostra de n x no qual ela se aproxima do valor da integral
n1=1
soma1=0
erro1 = 5 #qualquer numero maior que 0,01
xl=[]
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


#Metodo hit-miss
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
    if n2>10:
        erro2 = desvio_padrao_bernoulli(integral_estimada2)/(n2)**(1/2)
    #print(integral_estimada2)
    n2+=1

print("valor estimado:", integral_estimada2)
print("tamanho da amostra:", n2-1)
print("erro do hit-miss= ", erro2)






