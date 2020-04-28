def gauss(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n + 1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x
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
print(gauss(a))