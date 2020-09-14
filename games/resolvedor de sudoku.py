# contadores de tempo e de solucoes
import time

cont = 0


def Imprimamatriz(mat):
    for i in range(len(mat)):
        if i % 3 == 0 and i != 0:
            print("______________________________")

        for j in range(len(mat[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(mat[i][j])
            else:
                print(str(mat[i][j]) + " ", end="")


def TestaMatrizLida(mat):
    # testando se tem repetidos na linha
    for i in range(9):
        a = []
        for k in range(9):
            if mat[i][k] not in a and mat[i][k] != 0:
                a.append(mat[i][k])
            elif mat[i][k] in a and mat[i][k] != 0:
                return "linha"
    # testando se tem repetido na coluna
    for k in range(9):
        a = []
        for i in range(9):
            if mat[i][k] not in a and mat[i][k] != 0:
                a.append(mat[i][k])
            elif mat[i][k] in a and mat[i][k] != 0:
                return "coluna"
    # testando se tem repetido no bloco
    for L in range(0, 9, 3):
        for C in range(0, 9, 3):
            l = L // 3
            c = C // 3
            linf = l * 3 + 3
            colf = c * 3 + 3
            lini = l * 3
            coli = c * 3
            R = []

            for i in range(lini, linf):
                for j in range(coli, colf):
                    if mat[i][j] != 0 and mat[i][j] not in R:
                        R.append(mat[i][j])
                    elif mat[i][j] != 0 and mat[i][j] in R:
                        return "bloco"

    return "ok"


def TestaMatrizPreenchida(mat):
    if TestaMatrizLida(mat) != "ok":
        return False
    # testa se está totalmente preenchida
    for i in range(9):
        if 0 in mat[i]:
            return False
    return True


def LeiaMatrizLocal(NomeArquivo):
    # retorna a matriz lida se ok ou uma lista vazia senão
    #  #  # abrir o arquivo para leitura
    try:
        arq = open(NomeArquivo, "r")
    except:
        return []  # retorna lista vazia se deu erro
    # inicia matriz SudoKu a ser lida
    mat = [9 * [0] for k in range(9)]
    # ler cada uma das linhas do arquivo
    i = 0
    for linha in arq:
        v = linha.split()
        # verifica se tem 9 elementos e se são todos entre '1' e '9'
        # transforma de texto para int
        for j in range(len(v)):
            if v[j] <= "9" and v[j] >= "0":
                mat[i][j] = int(v[j])
            else:
                return "inválido"
        i += 1
    # faz as consistências iniciais da matriz dada
    # 3 possibilidades de erro
    if TestaMatrizLida(mat) == "linha":
        return "linha"
    if TestaMatrizLida(mat) == "coluna":
        return "coluna"
    if TestaMatrizLida(mat) == "bloco":
        return "bloco"

    # fechar arquivo e retorna a matriz lida e consistida
    arq.close()
    return mat


def ProcuraElementoLinha(Mat, L, d):
    for i in range(9):
        if Mat[L][i] == d:
            return i
    return -1


def ProcuraElementoColuna(Mat, C, d):
    for i in range(9):
        if Mat[i][C] == d:
            return i
    return -1


def ProcuraElementoQuadrado(Mat, L, C, d):
    l = L // 3
    c = C // 3
    linf = l * 3 + 3
    colf = c * 3 + 3
    lini = l * 3
    coli = c * 3
    for i in range(lini, linf):
        for j in range(coli, colf):
            if Mat[i][j] == d:
                return (i, j)
    return (-1, -1)


def vazio(mt):
    # procura indices vazios
    for i in range(9):
        for j in range(9):
            if mt[i][j] == 0:
                return (i, j)
    return None


def sudoku(Mat):
    global cont
    # resolve  o sudoku usando as funcoes criadas e imprime
    # usa o backtracking e retorna todas as solucoes possiveis
    nulo = vazio(Mat)
    if not nulo:
        return True
    else:
        L, C = nulo
    for p in range(1, 10):
        l = ProcuraElementoLinha(Mat, L, p)
        c = ProcuraElementoColuna(Mat, C, p)
        q = ProcuraElementoQuadrado(Mat, L, C, p)
        if l == c == -1 and q == (-1, -1):
            Mat[L][C] = p

            if sudoku(Mat) and TestaMatrizPreenchida(Mat):
                print("\n")
                print("* * * MATRIZ COMPLETA")
                Imprimamatriz(Mat)
                print("\n")
                cont += 1
            Mat[L][C] = 0
    return False


def rodar():
    # funcao que faz o programa funcionar
    a = "inicio"
    # consistências
    while a != "fim":
        global cont
        a = str(input("Entre com o nome do arquivo: "))
        if a == "fim":
            return
        if LeiaMatrizLocal(a) == "inválido":
            print("sudoku com números impróprios(maiores que 9 ou menores que 0)")
            a = str(input("Entre com o nome do arquivo: "))
            if a == "fim":
                return
        if LeiaMatrizLocal(a) == "linha":
            print("sudoku com linha imprópria(número repetido na mesma linha)")
            a = str(input("Entre com o nome do arquivo: "))
            if a == "fim":
                return
        if LeiaMatrizLocal(a) == "coluna":
            print("sudoku com coluna imprópria(número repetido na mesma coluna)")
            a = str(input("Entre com o nome do arquivo: "))
            if a == "fim":
                return
        if LeiaMatrizLocal(a) == "bloco":
            print("sudoku com bloco impróprio(número repetido no mesmo bloco)")
            a = str(input("Entre com o nome do arquivo: "))
            if a == "fim":
                return
        tempo1 = time.time()
        cont = 0
        print("* * * MATRIZ INICIAL * * *")
        m = LeiaMatrizLocal(a)
        Imprimamatriz(m)
        sudoku(m)
        tempo2 = time.time()
        tempogasto = tempo2 - tempo1
        print("* * * TEMPO DECORRIDO = ", tempogasto, "segundos")
        print("* * * ", cont, "SOLUCOES PARA ESSE SUDOKU")


rodar()

