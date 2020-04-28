def sem_pivo(Matriz):
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
a=[[2,2,4,8],[3,5,8,16],[9,21,29,59]]
print(sem_pivo(a))
print(a)







