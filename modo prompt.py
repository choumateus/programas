variaveis = []
valores=[] #listas para guardar as variaveis
#começamos o programa com a função que prioriza as operações
def prioridade(n):
    if n in  ["(",")"]:
        return 0
    if n == "=":
        return 1
    if n in ["+", "-"]:
        return 2
    if n in ["*", "/"]:
        return 3
    if n in ["#","_"]:
        return 4
    if n == "**":
        return 5
    if n >= "0" and n <= "9" or n == ".":
        return -2
    else :   #variável
        return -1
#funcao que separa cada variavel, operador ou operando em uma lista
def separa(op):
    op_sep =  []
    op = op.replace(" ","")
    item=""
    for p in range(len(op)):
        a = prioridade(op[p])
        if p != 0:
            if prioridade(op[p-1]) == a:
                if op[p] in ["/","=","+","-"]:
                    raise Exception ("expressao invalida")
                if op[p] == "*" and op[p-2] != op[p]:
                    item += op[p]
                if op[p] == "*" and op[p-2] == op[p]:
                    raise Exception ("expressao invalida")
                if a == -1 or a==-2:
                    item += op[p]
                if op[p-1]==op[p] and a==0:
                    op_sep.append(item)
                    item = op[p]
            if a != prioridade(op[p-1]):
                op_sep.append(item)
                if op[p] in ["+","-"] and op[p-1] in ["(","*","/","="]:
                    if op[p] == "+":
                        item = "#"
                    if op[p] == "-":
                        item = "_"
                else:
                    item=op[p]
        if p == 0:
            if a == 5 or a == 4 or a == 3:
                raise Exception ("expressao invalida")
            if op[p] == "+":
                item = "#"
            if op[p] == "-":
                item = "_"
            else:
                item += op[p]
        if p == len(op)-1:
            op_sep.append(item)
    #print(op_sep)
    return op_sep
#print(separa("(-2+4)-5+abc"))
#funcao do enunciado
def traduzposfixa(operacao):
    pilha=[]
    op=separa(operacao)
    pos=[]
    for i in range (len(op)):
        e=op[i]
        a=prioridade(e)
        if a < 0:
            pos.append(e)
        if a > 0:
            j=-1
            while j != -len(pilha)-1 and pilha[j]!="(":
                e1=pilha[j]
                a1=prioridade(e1)
                if a1 >= a:
                    pos.append(e1)
                    pilha.pop(j)
                else :
                    j-=1
            pilha.append(e)
        if a == 0:
            if e=="(":
                pilha.append(e)
            if e == ")":
                p=-1
                while pilha[p] != "(":
                    pos.append(pilha[p])
                    pilha.pop()
                pilha.pop()
    for j in range(-1,-len(pilha)-1,-1):
        pos.append(pilha[j])
    return pos
def calcula(operacao):
    global variaveis, valores
    op=traduzposfixa(operacao)
    pilha=[]
    #caso de atribuicao ex: a=3+54
    if "=" in op:
        for k in range(1,len(op)-1):    #na notacao posfixa a atribuicao,
            e=op[k]
            a=prioridade(e)
            if a<0:
                try:
                    pilha.append(float(e))
                except:
                    j=variaveis.index(op[k])
                    el=valores[j]
                    pilha.append(float(el))
            if a == 4:
                if e == "#":
                    pilha[len(pilha)-1] = (+1)*pilha[len(pilha)-1]
                if e == "_":
                    pilha[len(pilha) - 1] =(-1)*pilha[len(pilha) - 1]
            if a == 2:
                if e == "+":
                    pilha[len(pilha)-2]= pilha[len(pilha)-2]+pilha[len(pilha)-1]
                    pilha.pop()
                if e == "-":
                    pilha[len(pilha)-2]= pilha[len(pilha)-2]-pilha[len(pilha)-1]
                    pilha.pop()
            if a == 3:
                if e == "*":
                    pilha[len(pilha)-2]= pilha[len(pilha)-2]*pilha[len(pilha)-1]
                    pilha.pop()
                if e == "/":
                    pilha[len(pilha)-2]= pilha[len(pilha)-2]/pilha[len(pilha)-1]
                    pilha.pop()
            if a == 5:
                pilha[len(pilha) - 2] = pilha[len(pilha) - 2] ** pilha[len(pilha) - 1]
                pilha.pop()
        if op[0] in variaveis:
            i=variaveis.index(op[0])
            valores[i]= pilha[0]
            #valores.insert(i,pilha[0])
        if op[0] not in variaveis:
            variaveis.append(op[0])
            valores.append(pilha[0])
        return " "
    #caso de conta
    if "=" not in op:
        for k in range(len(op)):
            e=op[k]
            a=prioridade(e)
            if a<0:
                try:
                    pilha.append(float(e))
                except:
                    j=variaveis.index(op[k])
                    el=valores[j]
                    pilha.append(float(el))
            if a == 4:
                if e == "#":
                    pilha[len(pilha)-1] = (+1)*pilha[len(pilha)-1]
                if e == "_":
                    pilha[len(pilha) - 1] =(-1)*pilha[len(pilha) - 1]
            if a == 2:
                if e == "+":
                    pilha[len(pilha)-2]= pilha[len(pilha)-2]+pilha[len(pilha)-1]
                    pilha.pop()
                if e == "-":
                    pilha[len(pilha)-2]= pilha[len(pilha)-2]-pilha[len(pilha)-1]
                    pilha.pop()
            if a == 3:
                if e == "*":
                    pilha[len(pilha)-2]= pilha[len(pilha)-2]*pilha[len(pilha)-1]
                    pilha.pop()
                if e == "/":
                    pilha[len(pilha)-2]= pilha[len(pilha)-2]/pilha[len(pilha)-1]
                    pilha.pop()
            if a == 5:
                pilha[len(pilha) - 2] = pilha[len(pilha) - 2] ** pilha[len(pilha) - 1]
                pilha.pop()
        return pilha[0]
#funcao que roda o programa
def rodar():
    while True:
        try:
            conta=input(str(">>> "))
            print(calcula(conta))
        except:
            raise Exception("expressao invalida")
rodar()

