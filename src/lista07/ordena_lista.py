def input_int(msg, minimo, maximo, msg_err):
    while True:
        try:
            n = int(input(msg))
            if not minimo <= n <= maximo:
                raise ValueError(msg_err)
        except ValueError as e:
            print(e)
        else:
            break
    return n


def main():
    print("\n" * 5)
    nums_int = []
    n = 1
    while n != 0:
        n = input_int("Digite um número inteiro: ", -1,
                      10000, "Entre com um número de 0 a 100")
        if n != 0:
            nums_int.append(n)
    print(nums_int)
    nums_int.sort()
    print(nums_int)
    print(nums_int.count(4))


main()
