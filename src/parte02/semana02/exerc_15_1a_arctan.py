def arctan(x):
    """Recebe o número real x∈[0,1] e devolve uma aproximação do arco
    tangente de x (em radianos)"""
    if 0 <= x <= 1:
        arct = float(x)
        sinal = -1
        i = 3
        rep = True
        while rep:
            termo = sinal * (x ** i)/i
            arct += termo
            sinal = sinal * -1
            i += 2
            rep = abs(termo) > 0.00001
        return arct
    else:
        return "x fora do intervalo [0,1]"


def main():
    print(arctan(1))


if __name__ == "__main__":
    main()
