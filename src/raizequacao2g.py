from math import sqrt


def raizesEq2g(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('Não existem raízes reais para a equação')
    else:
        if delta == 0:
            x1 = -b / (2*a)
            print('uma raíz x=', str(x1))
        else:
            d = sqrt(delta)
            x1 = (-b + d) / (2*a)
            x2 = (-b - d) / (2*a)
            print('x1:', str(x1), 'e x2:', str(x2))


a1 = float(input("a: "))
b1 = float(input("b: "))
c1 = float(input("c: "))
raizesEq2g(a1, b1, c1)

#  x2 + x + 1 { , }
#  x2 - 5x + 6 {3, 2}
# 4x2 - 4x + 1 {0.5, 0.5}
#  x2 + 2x - 15 {3, -5}
