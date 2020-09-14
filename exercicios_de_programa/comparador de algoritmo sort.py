import time
import copy
#para o quick
class PilhaLista:
    def __init__(self):
        self._pilha = [] # lista que conterá a pilha
 # retorna o tamanho da pilha
    def __len__ (self):
        return len(self._pilha)
    # retorna True se pilha vazia
    def is_empty(self):
        return len(self._pilha) == 0
    def push(self, e):
        self._pilha.append(e)
    def pop(self):
        if self.is_empty():
            raise Exception("Pilha vazia")
        return self._pilha.pop()
#funcao que poe ano/mes/dia para comparar qual pessoa é mais velha
def verifica(tab):
    for i in range (1,len(tab)):
        if tab[i]<tab[i-1]:
            return False
    return True
def data_comparacao(data):
    nova=data[-4]+data[-3]+data[-2]+data[-1]+data[3]+data[4]+data[0]+data[1]
    return nova
def monta_tabela(arquivo,n):
    arq = open(arquivo, "r")
    tab=[]
    for linha in arq:
        itens = linha.split(",")
        tab.append([itens[0],itens[1],itens[2]])
    return tab[:n]
def voltadata(data):
    nova12=data[-2]+data[-1]+"/"+data[-4]+data[-3]+"/"+data[0]+data[1]+data[2]+data[3]
    return nova12
def pelo_sort(tab):
    tabs=copy.deepcopy(tab)
    ajusta(tabs)
    inicio = time.time()
    tabs.sort()
    fim = time.time()
    print("Método sort() do Python: ",(fim - inicio), "segundos")
    if verifica(tabs) == False:
        print("mal classificado")
    else:
        print("classificada")
def tabela_a_ser_printada(tab):
    tabs=copy.deepcopy(tab)
    ajusta(tabs)
    tabs.sort()
    ajusta_de_volta(tabs)
    return tabs
def ajusta_de_volta(tab):
    nova=tab[:]
    for i in range(len(tab)):
        nova[i][1]=voltadata(nova[i][1])
    return nova
def ajusta(tab):
    nova=tab[:]
    for i in range(len(tab)):
        nova[i][1]=data_comparacao(nova[i][1])
    return nova
def envia_tab(tab, nome):
    tabs=copy.deepcopy(tab)
    ajusta(tabs)
    tabs.sort()
    ajusta_de_volta(tabs)
    arq = open(nome, "w")
    for i in range(len(tabs)):
        arq.write(tabs[i][0] + "," + tabs[i][1] + "," + tabs[i][2])
    arq.close()
def particiona(lista, inicio, fim):
    i, j = inicio, fim
    dir = 1
    while i < j:
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
            dir = - dir
        if dir == 1:
            i = i + 1
        else:
            j = j - 1
    return i
def Quick_Sort_recursivo(lista, inicio, fim):
    # Se a lista tem mais de um elemento, ela será
    # particionada e as duas partições serão classificadas
    # pelo mesmo método Quick Sort
    if inicio < fim:
        k = particiona(lista, inicio, fim)
        Quick_Sort_recursivo(lista, inicio, k - 1)
        Quick_Sort_recursivo(lista, k + 1, fim)
def Quick_Sort(lista):
 # Cria a pilha de sub-listas e inicia com lista completa
    Pilha = PilhaLista()
    Pilha.push((0, len(lista) - 1))
 # Repete até que a pilha de sub-listas esteja vazia
    while not Pilha.is_empty():
        inicio, fim = Pilha.pop()
 # Só particiona se há mais de 1 elemento
        if fim - inicio > 0:
            k = particiona(lista, inicio, fim)
 # Empilhe as sub-listas resultantes
            Pilha.push((inicio, k - 1))
            Pilha.push((k + 1, fim))
def roda():
    print("Primeiramente: ")
    input("biscoito ou bolacha? ")
    input("nescau ou toddy? ")
    print("brincadeiras a parte, apenas para descontrair nesse final de semestre")
    print("____________________________________________________")
    print()
    print("INICIO DO PROGRAMA")
    while True:
        a=str(input("entre com o nome do arquivo de origem: "))
        if a=="fim":
            return
        b=str(input("entre com o nome do arquivo destino: "))
        c=int(input("Quantidade de registros a classificar: "))
        tabela=monta_tabela(a,c)
        tabelaquick=copy.deepcopy(tabela)
        ajusta(tabelaquick)
        tabelaquick1=copy.deepcopy(tabela)
        ajusta(tabelaquick1)
        envia_tab(tabela,b)
        pelo_sort(tabela)
        inicio1 = time.time()
        Quick_Sort_recursivo(tabelaquick,0,len(tabelaquick)-1)
        fim1 = time.time()
        print("Método quick recursivo: ",(fim1 - inicio1), "segundos")
        print("O QUICK EH RAPIDINHO NAO EH MSM? RS")
        if verifica(tabelaquick):
            print("classificada")
        else:
            print("nao esta classificada")
        inicio2 = time.time()
        Quick_Sort(tabelaquick1)
        fim2 = time.time()
        print("Método quick não recursivo: ", (fim2 - inicio2), "segundos")
        if verifica(tabelaquick1):
            print("classificada")
        else:
            print("nao esta classificada")
roda()
