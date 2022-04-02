def acha_max(matriz):
    '''Recebe uma matriz A e devolve 3 inteiros:
    k (um maior valor), e sua posicao lin, col.
    '''
    k = matriz[0][0]
    n_lin = len(matriz)
    n_col = len(matriz[0])
    for i in range(n_lin):
        for j in range(n_col):
            if matriz[i][j] >= k:
                k = matriz[i][j]
                lin = i
                col = j
    return k, lin, col


A = [[10, 7, 1],
     [1, 2, 8],
     [5, 3, 20]]
res = acha_max(A)

print(res)
