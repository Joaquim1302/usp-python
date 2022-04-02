def init_matriz(n_linhas, n_colunas, valor):
    """Cria uma matriz vazia de n_linhas x n_colunas"""
    matriz = []
    for _ in range(n_linhas):
        linha = []
        for _ in range(n_colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz


def mostra_matriz(matriz):
    """Exibe uma matriz em linhas e colunas"""
    for i in range(len(matriz)):
        linha = matriz[i]
        print(linha)


def main():
    matriz = init_matriz(4, 5, 0)
    matriz2 = [[10,   1,  20, - 5,   2],
               [0,  32,  15,  22, -10],
               [14,  25,  11, - 6,  30],
               [0, -35, -50,  12,  1]]
    mostra_matriz(matriz)
    print()
    mostra_matriz(matriz2)


main()
