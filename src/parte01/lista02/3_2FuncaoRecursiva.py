
# função recursiva
def verifica(n, d):
    if n == 0:
        return 0  # para n == 0 retorna a última chamada feita

    resto = n % 10  # resto é o último digito do número
    if resto % 10 == d:
        c = 1
    else:
        c = 0

    co = c + verifica(n // 10, d)  # encadeamento das chamadas
    # retorno das chamadas

    return co


def verifica2(n, d):
    i = n
    c = 0
    while i > 0:
        if i % 10 == d:
            c += 1
        i //= 10
    return c


# n0 = int(input("Digite o valor de n (n > 0): "))
# d0 = int(input("Digite o valor de d (0<=d<=9): "))
n0, d0 = 2937719877, 7
print(f'O número {d0} ocorre {verifica2(n0, d0)} vezes no número {n0}')
