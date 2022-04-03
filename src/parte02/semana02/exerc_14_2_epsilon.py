def fatorial(n):
    """calcula o fatorial de de um número"""
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


def epsilon(x):
    eps = 1.0 + x
    i = 2
    aprox = True
    while aprox:
        termo = (x ** i) / fatorial(i)
        eps += termo
        aprox = not abs(termo) < (x / 100)
        i += 1
    return eps


def get_exp(n):
    return 2.718281828459045 ** n


def main():
    for j in range(10):
        print(epsilon(float(j+1)), get_exp(j + 1))


if __name__ == "__main__":
    main()
