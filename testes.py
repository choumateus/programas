def sol(Matriz):
    n=len(Matriz)
    x = [0 for i in range(n)]
    for i in range(n):
        try:
            x[i] = Matriz[i][n] / Matriz[i][i]
        except:
            return "sem solucao unica"  # caso de divisao por 0
        for k in range(i,n):
            Matriz[k][n] -= Matriz[k][i] * x[i]
    return x
a=[[1,0,0,1],[2,3,0,5],[6,3,7,16]]
print(sol(a))