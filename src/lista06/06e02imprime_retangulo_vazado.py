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


def print_retangulo_vazado(a, b):
    i = 1
    while i <= b:
        j = 1
        while j <= a:
            if (2 <= j < a) and i != 1 and i != b:
                print(" ", end="")
            else:
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
    print_retangulo_vazado(a, b)


main()
