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
    def __init__(self, aero= "AAA", comp="AA-000"):
        self.aeroporto = aero
        self.companhia = comp
