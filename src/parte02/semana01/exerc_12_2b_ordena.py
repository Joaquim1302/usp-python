def acha_maximo(matriz):
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


def acha_min(matriz):
    '''Recebe uma matriz A e devolve 3 inteiros:
    k (um maior valor), e sua posicao lin, col.
    '''
    k = matriz[0][0]
    n_lin = len(matriz)
    n_col = len(matriz[0])
    for i in range(n_lin):
        for j in range(n_col):
            if matriz[i][j] <= k:
                k = matriz[i][j]
                lin = i
                col = j
    return k, lin, col


def main():
    mat_a = [[3, 7, 1],
             [1, 2, 8],
             [5, 3, 4]]

    minimo = acha_min(mat_a)
    m = len(mat_a) * len(mat_a[0])
    print("Elem   Linha  Coluna")
    for _ in range(m):
        maximo = acha_maximo(mat_a)
        mat_a[maximo[1]][maximo[2]] = minimo[0]
        print(f'{maximo[0]:3d}{maximo[1]:7d}{maximo[2]:7d}')


main()
