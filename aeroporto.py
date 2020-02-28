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
    def __init__(self, aero= "AAA", comp="AA", num = 000, temp = 0, situ = "P",emerg = "N",pouso_decolagem = 2):
        self.aeroporto = aero
        self.companhia = comp
        self.num = num
        self.temp = temp  # seja combustivel ou tempo estimado de voo
        self.situ =situ  # P para pousando, D para decolando
        self.pouso_decolagem = pouso_decolagem
        self.emerg = emerg
    def emergencia(self):
        return self.emerg == "S"
    def passou(self):
        if self.pouso_decolagem > 0:
            return False


class pistas:
    def __init__(self):
        self.pistas= [None,None,None]
    def vazio(self):
        if None in self.pistas:
            return True
        else:
            return False
    def append(self, a):
        for i in range(len(self.pistas)):
            if self.pistas[i]==None:
                self.pistas[i] = a
                break
pistas = pistas()
testes = random.randint(10, 30)
nums = "0123456789"
situs = "PD"
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(testes):
    k = random.randint(0,3)
    for j in range (k):
        aero = letras[random.randint(0,25)] + letras[random.randint(0,25)] + letras[random.randint(0,25)]
        comp =  letras[random.randint(0,25)] + letras[random.randint(0,25)]
        num = int(nums[(random.randint(0,9))]+nums[(random.randint(0,9))]+nums[(random.randint(0,9))])
        temp = int(nums[(random.randint(0,9))])
        situ = situs[random.randint(0,1)]
        if random.randint(1,10) == 1:
            aviao = aviao(aero,comp,num,temp,situ, "S")
        else:
            aviao = aviao(aero,comp,num,temp,situ)
        if pistas.vazio():
            pistas.append(aviao)








