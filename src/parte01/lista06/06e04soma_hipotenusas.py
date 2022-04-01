def é_hipotenusa(a):
    a2 = a ** 2
    b = 1
    while b < a:
        c = 1
        while c < a:
            if a2 == b ** 2 + c ** 2:
                # print(str(a) + "^2 = " + str(b) +
                #       "^2 + " + str(c) + "^2", end=" : ")
                return True
            c += 1
        b += 1
    return False


def soma_hipotenusas(n):
    soma = 0
    a = 1
    while a <= n:
        if é_hipotenusa(a):
            # print(a)
            soma += a
        a += 1
    return soma


# print(soma_hipotenusas(25))
