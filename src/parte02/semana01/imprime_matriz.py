"""Exercício Op 01: Imprimindo matrizes"""


def imprime_matriz(matriz):
    n_lin = len(matriz)
    n_col = len(matriz[0])
    for i in range(n_lin):
        for j in range(n_col):
            print(matriz[i][j], end="")
            if j < n_col-1:
                print(end=" ")
        print()


minha_matriz = [[1], [2], [3]]
imprime_matriz(minha_matriz)
print()
minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
