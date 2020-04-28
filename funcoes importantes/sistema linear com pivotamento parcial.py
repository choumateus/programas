def pivotamento_parcial(Matriz):
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
        # Swap maximum row with current row (column by column)
        #for k in range(i, n + 1):
            #tmp = Matriz[maxRow][k]
            #Matriz[maxRow][k] = Matriz[i][k]
            #Matriz[i][k] = tmp

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
a=[[2,2,4,8],[3,5,8,16],[9,21,23,53]]
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
a=gerador(16)
print(a)
print(pivotamento_parcial(a))
print(a)