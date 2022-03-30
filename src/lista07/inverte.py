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
    nums_int = []
    n = 1
    while n != 0:
        n = input_int("Digite um número: ", -1,
                      10000, "Entre com um número de 0 a 100")
        if n != 0:
            nums_int.append(n)
    for i in range(len(nums_int), 0, -1):
        print(nums_int[i - 1])


main()
