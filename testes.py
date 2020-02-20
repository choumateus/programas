import numpy as np
class fila:
    def __init__(self):
        self.fila = [] #construtor
    def vazio(self):
        return len(self.fila) == 0
    def insere(self, i):
        self.fila.append(i)
    def tira(self):
        if self.vazio():
            raise Exception ("fila vazia")
        return self.fila.pop(0)
    def primeiro(self):
        if self.vazio():
            raise Exception ("fila vazia")
        return self.fila[0]
    def __getitem__(self, i):
        return self.fila[i]
    def __setitem__(self, i, j):
        self.fila[i] = j
    def mostre(self):
        print(self.fila)
    #def preferencial(self, i):

a=fila()
b=fila()
a.insere(0)
a.insere(1)
a.insere(2)
a.insere(3)
a[0] , a[1] = a[1], a[0]
a.mostre()
a=np.array([2,3,4,5,1,12,3,1])
a[0]=1
print(a)
