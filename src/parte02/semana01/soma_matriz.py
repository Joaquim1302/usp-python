"""Exercício 2: Soma de matrizes"""


def soma_matrizes(m_1, m_2):
    if (len(m_1) == len(m_2)) and (len(m_1[0]) == len(m_2[0])):
        n_lin = len(m_1)
        n_col = len(m_1[0])
        for i in range(n_lin):
            for j in range(n_col):
                m_1[i][j] += m_2[i][j]
    else:
        return False
    return m_1


def soma_matrizes2(m_1, m_2):
    if (len(m_1) == len(m_2)) and (len(m_1[0]) == len(m_2[0])):
        for i, linha in enumerate(m_1):
            for j, iten in enumerate(linha):
                iten += m_2[i][j]
    else:
        return False
    return m_1


print("\n" * 5)
ma = [[1, 2, 3], [4, 5, 6]]
mb = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(ma, mb))
print(soma_matrizes2(ma, mb))
print()
ma = [[1], [1]]
mb = [[2], [5]]
print(soma_matrizes(ma, mb))
print()

ma = [[1]]
mb = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
print(soma_matrizes(ma, mb))
