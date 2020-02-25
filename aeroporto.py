import random
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
class aviao:
    def __init__(self, aero= "AAA", comp="AA", num = 000, temp = 0, situ = "P"):
        self.aeroporto = aero
        self.companhia = comp
        self.num = num
        self.temp = temp  # seja combustivel ou tempo estimado de voo
        self.situ =situ       # P para pousando, D para decolando
pistas = [None,None,None] #3 eh apens para decolagema ao menos de emergencia
testes = random.randint(10, 30)
num = "0123456789"
situs = "PD"
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(testes):
    k = random.randint(0,3)
    for j in range (k):
        aero = letras[random.randint(0,25)]
        if None not in pistas:





