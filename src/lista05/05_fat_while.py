def inputInt(msg, minimo, maximo, msgErr):
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


def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


print("\n" * 5)
n = 1
while n >= 0:
    n = inputInt("Digite um número inteiro: ", -1, 100,
                 "Entre com um número de 0 a 100")

    print("Fatorial: ", fatorial(n))
    print("\n")
