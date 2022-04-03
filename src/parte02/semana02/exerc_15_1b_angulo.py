import exerc_15_1a_arctan

P_I = 3.14159265359


def to_graus(rads):
    return 180 * rads / P_I


def angulo_graus(x, y):
    """recebe um ponto de coordenadas cartesianas reais (x,y),
    com x>0 e y>0 e devolve o ângulo formado pelo vetor (x,y)
    e o eixo horizontal."""
    if y < x:
        arc_tan = exerc_15_1a_arctan.arctan(y / x)
    else:
        arc_tan = P_I / 2 - exerc_15_1a_arctan.arctan(x / y)
    ang = to_graus(arc_tan)
    return ang


def main():
    print(angulo_graus(0, 1))
    print(angulo_graus(2, 2))
    print(angulo_graus(1, 4))
    print(angulo_graus(5, 1))


if __name__ == "__main__":
    main()
