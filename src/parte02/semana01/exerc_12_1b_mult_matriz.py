def mat_init(n_linhas, n_colunas, valor):
    """Cria uma matriz vazia de n_linhas x n_colunas"""
    matriz = []
    for _ in range(n_linhas):
        linha = []
        for _ in range(n_colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz


def mat_imprime(matriz):
    """Mostra uma matriz"""
    n_lin = len(matriz)
    n_col = len(matriz[0])
    if n_lin > 0 and n_col > 0:
        for i in range(n_lin):
            for j in range(n_col):
                print(f"{matriz[i][j]:4d}", end="")
            print()


def mat_sao_multiplicaveis(mat_1, mat_2):
    """Retorna True se as matrizes são multiplicáveis"""
    cl_m_1 = len(mat_1[0])
    ln_m_2 = len(mat_2)
    return cl_m_1 == ln_m_2


def produto_lincol(lin, a_mat, col, b_mat):
    """Recebe duas matriz a_mat e b_mat e dois inteiros lin e col
    e calcula a soma o produto entre a linha lin de a_mat com
    a coluna col de b_mat"""

    linha_a = a_mat[lin]
    prd = 0
    n = len(b_mat)
    for i in range(n):
        prd += linha_a[i] * b_mat[i][col]
    return prd


def mat_produto(a_mat, b_mat):
    """Recebe duas matrizes a_mat mxn e b_mat nxp e calcula o produto
    entre a_mat e b_mat"""

    if mat_sao_multiplicaveis(a_mat, b_mat):
        m = len(a_mat)
        p = len(b_mat[0])
        c_mat = mat_init(m, p, 0)
        for i in range(m):
            for j in range(p):
                c_mat[i][j] = produto_lincol(i, a_mat, j, b_mat)
        return c_mat

    else:
        print("Não são multiplicáveis.")
        return [[]]


# A = [[2, 3],
#      [0, 1],
#      [-1, 4]]
# B = [[1, 2, 3],
#      [-2, 0, 4]]
# A x B
#   -4   4  18
#   -2   0   4
#   -9  -2  13
# B x A
#   -1  17
#   -8  10


# A = [[2, 3, 1],
#      [-1, 0, 2]]
# B = [[1, -2],
#      [0, 5],
#      [4, 1]]
# 6  12
# 7   4

# A = [[3, 2],
#      [5, -1]]
# B = [[6, 4, -2],
#      [0, 7, 1]]
#   18  26  -4
#   30  13 -11

A = [[1, 2, 3]]
B = [[3],
     [2],
     [1]]
#   10

mat_imprime(A)
print()
mat_imprime(B)
print()
mat_imprime(mat_produto(A, B))
