def sao_multiplicaveis(mat_1, mat_2):
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


def produto_lincol_bak(lin, a_mat, col, b_mat):
    """Recebe duas matriz a_mat e b_mat e dois inteiros lin e col
    e calcula a soma o produto entre a linha lin de a_mat com
    a coluna col de b_mat"""
    prd = 0

    i = 0
    while i < len(a_mat):
        prd += a_mat[lin][i] * b_mat[i][col]
        i += 1
    return prd


A = [[1, 2, 1],
     [2, 2, 2],
     [1, 3, 2]]
B = [[1, 1],
     [2, 0],
     [0, 1]]

if sao_multiplicaveis(A, B):
    print(produto_lincol(1, A, 0, B))
    print(produto_lincol(0, A, 1, B))
    print(produto_lincol(1, A, 1, B))
    print(produto_lincol(0, A, 0, B))
else:
    print("Não são multiplicáveis.")
