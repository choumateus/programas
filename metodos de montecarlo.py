from random import randrange
import math as mt

#primeiro vamos estimar um valor muito proximo do valor da intergral que queremos calcular
#para isso vamos simular varias vezes monte carlo e achar a media de todas as simulacoes
b=11221352   #NUSP
a=501925028   #RG
def f(x):
    return mt.e**(-a*x)*mt.cos(b*x)
