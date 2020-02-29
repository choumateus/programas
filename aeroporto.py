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
    def passou_tempo(self):
        if self.pouso_decolagem > 0:
            self.pouso_decolagem-=1
            return False
        else:
            return True
    def esvazia(self):
        self.existe = 0
    def existe(self):
        return self.existe == 1
    def __str__(self):
        if self.existe == 1:
            return "companhia : " + str(self.companhia) + " numero: " + str(self.num) + " aeroporto: " + str(self.aeroporto)
        else :
            return "vazia"
class pistas:
    def __init__(self):
        self.pistas= [None,None]
    def vazio(self):
        if  self.pistas[0].existe():
            return False
        else:
            return True
    def append(self, a):
        for i in range(len(self.pistas)):
            if self.pistas[i]==None:
                self.pistas[i] = a
                break
    def __len__(self):
        return len(self.pistas)
    def __getitem__(self, i):
        return self.pistas[i]
    def __setitem__(self, i, j):
        self.pistas[i] = j
    def __str__(self):
        return "pista 1: " + str(self.pistas[0]) +  "\n pista 2: " + str(self.pistas[1]) + "\n pista 3: " + str(pistas[2])
pistas = pistas()
testes = random.randint(10, 30)
nums = "0123456789"
situs = "PD"
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(testes):
    k = random.randint(0,3) #quantidade de avioes que vao entrar
    for m in range (len(pistas)):
        if pistas[m] != None:
            if pistas[m].passou_tempo():
                pistas[m].esvazia()
    for j in range (k):
        aero = letras[random.randint(0,25)] + letras[random.randint(0,25)] + letras[random.randint(0,25)]
        comp =  letras[random.randint(0,25)] + letras[random.randint(0,25)]
        num = int(nums[(random.randint(0,9))]+nums[(random.randint(0,9))]+nums[(random.randint(0,9))])
        temp = int(nums[(random.randint(0,9))])
        situ = situs[random.randint(0,1)]
        if random.randint(1,10) == 1:
            A= aviao(aero,comp,num,temp,situ, "S")
        else:
            A = aviao(aero,comp,num,temp,situ)
        if pistas.vazio():
            pistas.append(aviao)








