nums = [1, 5, 8, 13, 17, 35]


def input_int(msg, minimo, maximo, msgErr):
    while True:
        try:
            n = int(input(msg))
            if not (minimo <= n <= maximo):
                raise ValueError(msgErr)
        except ValueError as e:
            print(e)
        else:
            break
    return n


def fat_prime(n):
    fator = 2
    multiplicidade = 0
    while n > 1:
        while n % fator == 0:
            multiplicidade += 1
            n /= fator
        if multiplicidade > 0:
            print("fator", fator, "multiplicidade =", multiplicidade)
        fator += 1
        multiplicidade = 0


print("\n" * 5)
n0 = 1
while n0 >= 0:
    n0 = input_int("Digite um número inteiro: ", -1, 10000,
                   "Entre com um número de 0 a 100")
    fat_prime(n0)

    print("\n")
