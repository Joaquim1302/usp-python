def sao_multiplicaveis(mat_1, mat_2):
    cl_m_1 = len(mat_1[0])
    ln_m_2 = len(mat_2)
    return cl_m_1 == ln_m_2


def produto_lincol(lin, a_mat, col, b_mat):
    """Recebe duas matriz a_mat e b_mat e dois inteiros lin e col
    e calcula a soma o produto entre a linha lin de a_mat com
    a coluna col de b_mat"""
    prd = 0
    if sao_multiplicaveis(a_mat, b_mat):
        i = 0
        while i < len(a_mat):
            prd += a_mat[lin][i] * b_mat[i][col]
            i += 1
        print(prd)
    else:
        print("Não são multiplicáveis.")


A = [[1, 2, 1],
     [2, 2, 2],
     [1, 3, 2]]
B = [[1, 1],
     [2, 0],
     [0, 1]]
produto_lincol(1, A, 0, B)
