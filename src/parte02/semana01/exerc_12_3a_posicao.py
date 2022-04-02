def mat_imprime(matriz):
    """Mostra uma matriz"""
    n_lin = len(matriz)
    n_col = len(matriz[0])
    if n_lin > 0 and n_col > 0:
        for i in range(n_lin):
            for j in range(n_col):
                print(f"{matriz[i][j]:4d}", end="")
            print()


def conta_bomba(matriz, lin, col):
    if lin > 0:
        x_0 = lin - 1
    else:
        x_0 = 0
    if col > 0:
        y_0 = col - 1
    else:
        y_0 = 0
    if lin + 1 < len(matriz):
        lin += 1
    if col + 1 < len(matriz[0]):
        col += 1

    mat_imprime(A)
    print()
    i = x_0
    n_bombas = 0
    while i <= lin:
        j = y_0
        while j <= col:
            if A[i][j] == 1:
                n_bombas += 1
                A[i][j] = 6
            else:
                A[i][j] = 8
            j += 1
        i += 1

    mat_imprime(A)
    print(f"{n_bombas:2d} bombas")


A = [
    # 0  1  2  3  4  5
    [0, 0, 0, 0, 0, 0],  # 0
    [0, 1, 0, 0, 0, 0],  # 1
    [0, 0, 0, 0, 0, 0],  # 2
    [0, 1, 0, 1, 1, 0],  # 3
    [0, 0, 1, 1, 0, 0],  # 4
    [0, 1, 0, 0, 0, 1],  # 5

]


conta_bomba(A, 3, 3)
