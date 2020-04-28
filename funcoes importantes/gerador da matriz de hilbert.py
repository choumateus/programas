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
print(gerador(4))