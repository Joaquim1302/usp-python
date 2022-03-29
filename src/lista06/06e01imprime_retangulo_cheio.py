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


def print_retangulo_cheio(a, b):
    i = 0
    while i < b:
        j = 0
        while j < a:
            print("#", end="")
            j += 1
        print()
        i += 1


def main():
    print("\n" * 5)
    a = inputInt("digite a largura: ", -1, 1000,
                 "Entre com um número de 0 a 1000")
    b = inputInt("digite a altura: ", -1, 1000,
                 "Entre com um número de 0 a 1000")
    print("\n")
    print_retangulo_cheio(a, b)
    print("\n")


main()
