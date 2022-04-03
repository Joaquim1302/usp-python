def aprox_raiz(x, precisao):
    raiz = x
    # print(raiz, end="  ")

    for i in range(1, precisao + 1):
        raiz = (raiz + x / raiz) / 2
        # print(raiz, end="  ")
    # print()
    return raiz


def main():
    print(aprox_raiz(3, 4))
    print(aprox_raiz(4, 4))
    print(aprox_raiz(5, 4))
    print(aprox_raiz(0.81, 4))


if __name__ == "__main__":
    main()
