def gerador(n):
    mat=[[0 for i in range(n+1)]for j in range(n)]
    n = len(mat)
    for i in range(n):
        for j in range(n):
            mat[i][j] = 1/(i+j+1) #somamos 1 , pois o index do python comeca do 0 e nao do 1, logo temos ((i+1)+(j+1)-1)
    for i in range(n):            #que é igual a i+j+1
        for j in range(n):
            mat[i][-1]+=mat[i][j]
    return mat
a=gerador(4)
b=gerador(4)
def sem_pivo(n):
    Matriz= gerador(n)
    n = len(Matriz)
    if len(Matriz) != len(Matriz[0])-1:
        return "sem solucao"
    for i in range(0, n):
        #escalonando a matriz
        for k in range(i + 1, n):
            c = Matriz[k][i] / Matriz[i][i]
            for j in range(i, n + 1):
                Matriz[k][j] -= c * Matriz[i][j]

    # monta e soluciona a equacao, com a matriz triangular
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        try:
            x[i] = Matriz[i][n] / Matriz[i][i]
        except:
            return "sem solucao unica" #caso de divisao por 0
        for k in range(i - 1, -1, -1):
            Matriz[k][n] -= Matriz[k][i] * x[i]
    return x
def pivotamento_parcial(n):
    Matriz = gerador(n)
    if len(Matriz) != len(Matriz[0]) - 1:
        return "sem solucao"
    n = len(Matriz)

    # encontrando o maior elemento da coluna para realizar a troca
    for i in range(0, n):
        maxEl = Matriz[i][i]
        maxRow = i
        for k in range(i + 1, n):
            if Matriz[k][i] > maxEl:
                maxEl = Matriz[k][i]
                maxRow = k

        if i!=maxRow:
            Matriz[maxRow], Matriz[i] = Matriz[i] , Matriz[maxRow]

        # escalonando a matriz#
        for k in range(i + 1, n):
            c = Matriz[k][i] / Matriz[i][i]
            for j in range(i, n + 1):
                Matriz[k][j] -= c * Matriz[i][j]

        # monta e soluciona a equacao, com a matriz triangular
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        try:
            x[i] = Matriz[i][n] / Matriz[i][i]
        except:
            return "sem solucao unica" #caso de divisao por 0
        for k in range(i - 1, -1, -1):
            Matriz[k][n] -= Matriz[k][i] * x[i]
    return x
def norma_2(x):
    soma=0
    for i in range(len(x)):
        soma+= (x[i]-1)**2
    return (soma)**(1/2)
def determinante(Matriz):
    n = len(Matriz)
    deter=1
    for i in range(0, n):
        #escalonando a matriz
        for k in range(i + 1, n):
            c = Matriz[k][i] / Matriz[i][i]
            for j in range(i, n + 1):
                Matriz[k][j] -= c * Matriz[i][j]
    for i in range(n):
        deter*=Matriz[i][i]
    return(deter)
print("*************             PARTE 1               ****************" )
rodar = "sim"
n=2
while rodar != "nao":
    print(sem_pivo(n))
    print()
    print("norma 2 do vetor x da solucao sem pivo com o a solucao oficial", norma_2(sem_pivo(n)))
    print()
    print("determinante da matriz de hilbert", determinante(gerador(n)))
    print()
    print(pivotamento_parcial(n))
    print()
    print("norma 2 do vetor x da solucao com pivotamento parcial com o a solucao oficial", norma_2(pivotamento_parcial(n)))
    print()
    n *= 2
    rodar = input("continuo rodando esse programa? (sim ou nao) ")
