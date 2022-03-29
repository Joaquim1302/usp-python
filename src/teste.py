def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


def ehLetra(c):
    ac = ord(c)
    a = (ac >= 65 and ac <= 90)
    b = (ac >= 97 and ac <= 122)
    c = a or b
    return c


def inputInt(msg, min, max, msgErr):
    while True:
        try:
            n = int(input(msg))
            if not min <= n <= max:
                raise ValueError(msgErr)
        except ValueError as e:
            print(e)
        else:
            break
    return n


# pecas = inputInt("Quantas peças você vai tirar? ", 1, 5,
#                  "Oops! Jogada inválida! Tente de novo.")
# print(pecas)

def multiplo(n):
    for x in range(1, n):
        if (n % x == 0):  # se o resto da divisão de n/x for 0 (múltiplo)
            print(x)  # múltiplo


multiplo(1)
multiplo(2)
multiplo(3)
multiplo(4)
multiplo(5)
