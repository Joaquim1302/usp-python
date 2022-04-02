def maiusculas(frase):
    ascii_ma = [65, 90]
    # ascii_mi = [97, 122]
    m = ""
    for c in frase:
        c_dec = ord(c)
        if ascii_ma[0] <= c_dec <= ascii_ma[1]:
            m += c
    return m

# print(maiusculas("Programamos em python 2?"))
# print(maiusculas("Programamos em Python 3."))
# print(maiusculas("PrOgRaMaMoS em python!"))
