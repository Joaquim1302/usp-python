"""Exercício Op 02: Matrizes multiplicáveis"""


def sao_multiplicaveis(mat_1, mat_2):
    cl_m_1 = len(mat_1[0])
    ln_m_2 = len(mat_2)
    return cl_m_1 == ln_m_2


m_1 = [[1, 2, 3], [4, 5, 6]]
m_2 = [[2, 3, 4], [5, 6, 7]]
print(sao_multiplicaveis(m_1, m_2))
print()
m_1 = [[1], [2], [3]]
m_2 = [[1, 2, 3]]
print(sao_multiplicaveis(m_1, m_2))
