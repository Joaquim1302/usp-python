def init_matriz(n_linhas, n_colunas, valor):
    """Cria uma matriz vazia de n_linhas x n_colunas"""
    matriz = []
    for _ in range(n_linhas):
        linha = []
        for _ in range(n_colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz


def main():
    matriz = init_matriz(4, 5, 0)
    print(matriz)


main()
