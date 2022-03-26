from math import sqrt
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = b ** 2 - 4 * a * c
if delta < 0:
    print('esta equação não possui raízes reais')
else:
    if delta == 0:
        x1 = -b / (2*a)
        print('a raiz dupla desta equação é', str(x1))
    else:
        d = sqrt(delta)
        x1 = (-b - d) / (2*a)
        x2 = (-b + d) / (2*a)
        print('as raízes da equação são', str(x1), 'e', str(x2))
