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

def tabuada():
    tab = 1
    while tab <= 10:
        print("Tabuada do", tab, ":", end="\t")
        i = 1
        print(tab*i, end="\t")
        i = i + 1
        print()
        tab = tab + 1


tabuada()
