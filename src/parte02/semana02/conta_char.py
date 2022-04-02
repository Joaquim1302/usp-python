def eh_minuscula(c):
    ac = ord(c)
    return ac >= 97 and ac <= 122


def eh_vogal(c):
    vogais = ["a", "e", "i", "o", "u"]
    letra = c.lower()
    return letra in vogais


def eh_consoante(c):
    c = c.lower()
    return eh_minuscula(c) and not eh_vogal(c)


def conta_letras(frase, contar="vogais"):
    comp_frase = len(frase)
    i = 0
    n_vogais = 0
    n_consoantes = 0
    while i < comp_frase:
        if eh_vogal(frase[i]):
            n_vogais += 1
        elif eh_consoante(frase[i]):
            n_consoantes += 1
        i += 1
    if contar == "vogais":
        n = n_vogais
    elif contar == "consoantes":
        n = n_consoantes
    else:
        n = comp_frase - n_consoantes - n_vogais

    return n


# print(conta_letras('programamos em python'))
# print(conta_letras('programamos em python', 'vogais'))
# print(conta_letras('  programamos em python', 'consoantes'))
