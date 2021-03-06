import random
class fila:

    def __init__(self):
        self.fila = [] #construtor

    def __len__(self):
        return len(self.fila)

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

    def __str__(self):
        if len(self.fila) > 0:
            return str(self.fila[-1])
        return str(None)
class aviao:
    def __init__(self, aero= "AAA", comp="AA", num = 000, temp = 0, situ = "P",emerg = "N",pouso_decolagem = 2, existencia = 1):
        self.aeroporto = aero
        self.companhia = comp
        self.num = num
        self.temp = temp  # seja combustivel ou tempo estimado de voo
        self.situ =situ  # P para pousando, D para decolando
        self.pouso_decolagem = pouso_decolagem
        self.emerg = emerg
        self.existencia = existencia
    def emergencia(self):
        if  self.emerg == "S" or self.temp==0:
            return True
        else:
            return False
    def acabando(self):
        if self.temp == 0:
            return True
        else:
            return False
    def passou_tempo(self):
        if self.pouso_decolagem >= 0:
            #print("ainda nao")
            return False
        elif self.pouso_decolagem == -1:
            #print("deu 0")
            return True
    def esvazia(self):
        self.existencia = 0
    def __str__(self):
        if self.existencia == 1:
            return "companhia : " + str(self.companhia) + " numero: " + str(self.num) + " aeroporto: " + str(self.aeroporto) + " emergencial? " + str(self.emerg)
        elif self.existencia == 0 :
            return "vazia"
    def reduz_tempo(self):
        self.pouso_decolagem-=1
    def existe(self):
        return self.existencia == 1
class pistas:
    def __init__(self):
        self.pistas= [aviao(existencia=0),aviao(existencia=0),aviao(existencia=0)]
    def append(self, a):
        for i in range (len(pistas)):
            if pistas[i].existencia==0:
                self.pistas[i] = a
                return 1 #inseriu na pista
        return 0 #nao inseriu na pista
    def append_emergencial(self,a):
        for i in range(len(pistas)):
            if pistas[i].temp < 2 :
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
fila = fila( )
testes = random.randint(10, 30)
nums = "0123456789"
situs = "PD"
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def testar():
    for i in range(testes):
        k = random.randint(0,3) #quantidade de avioes que vao entrar
        for m in range (len(pistas)): #passando o tempo
            if pistas[m].existe():
                if not  pistas[m].passou_tempo():
                    pistas[m].reduz_tempo()
                if pistas[m].passou_tempo():
                    pistas[m].existencia = 0
        contador_de_inseridos = 0
        for n in range (len(fila)): #inserindo os que estao na fila
            if not fila.vazio():
                if fila[n].emergencia():
                    #print(len(fila))
                    pistas.append_emergencial(fila[n])
                    contador_de_inseridos+=1
                else:
                    if pistas.append(fila[n]) == 1:
                        contador_de_inseridos +=1
            #print(contador_de_inseridos)
        for b in range(contador_de_inseridos): #retirando da fila
            fila.tira()
        for j in range (k):
            novo = 0
            aero = letras[random.randint(0,25)] + letras[random.randint(0,25)] + letras[random.randint(0,25)]
            comp =  letras[random.randint(0,25)] + letras[random.randint(0,25)]
            num = int(nums[(random.randint(0,9))]+nums[(random.randint(0,9))]+nums[(random.randint(0,9))])
            temp = int(nums[(random.randint(0,1))]+nums[(random.randint(0,9))])
            situ = situs[random.randint(0,1)]
            aviao1 = aviao(aero,comp,num,temp,situ)
            if random.randint(1,10) == 1:
                aviao1.emerg="S"
                novo =1
                pistas.append_emergencial(aviao1)
            else:
                novo = pistas.append(aviao1)
            if novo == 0 :
                fila.insere(aviao1)
        print(pistas)
def finalizar(): #para finalizar a fila e fechar o aeroporto
    print("retirando")
    while len(fila) > 0:
        for m in range (len(pistas)): #passando o tempo
            if pistas[m].existe():
                if not  pistas[m].passou_tempo():
                    pistas[m].reduz_tempo()
                if pistas[m].passou_tempo():
                    pistas[m].existencia = 0
        contador_de_inseridos = 0
        for n in range (len(fila)): #inserindo os que estao na fila
            if not fila.vazio():
                if fila[n].emergencia():
                    #print(len(fila))
                    pistas.append_emergencial(fila[n])
                    contador_de_inseridos+=1
                else:
                    if pistas.append(fila[n]) == 1:
                        contador_de_inseridos +=1
            #print(contador_de_inseridos)
        for b in range(contador_de_inseridos): #retirando da fila
            fila.tira()
        print(pistas)
    for j in range (3):
        for m in range(3):  # passando o tempo
            if pistas[m].existe():
                if not pistas[m].passou_tempo():
                    pistas[m].reduz_tempo()
                if pistas[m].passou_tempo():
                    pistas[m].existencia = 0
        print(pistas)
    print()
    print(" ***********Aeroporto fechado************* ")
testar()
finalizar()









