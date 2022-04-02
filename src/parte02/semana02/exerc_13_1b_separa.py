def separa(texto, sep):
    n_texto = len(texto)
    n_sep = len(sep)
    i = 0
    txt = []
    stt = ""
    while i < n_texto:
        if n_sep == 0:
            txt.append(texto[i])
        elif texto[i] == sep:
            txt.append(stt)
            stt = ""
        else:
            stt += texto[i]
        i += 1
    if len(stt) > 0:
        txt.append(stt)
    return txt


def tam_maior_palavra(txt):
    maior = len(txt[0])
    for word in txt:
        l_word = len(word)
        if l_word > maior:
            maior = l_word

    return maior


def main():
    txt = "Usando,a,função,do,item,anterior,escreva,um,programa,que," + \
        "leia,uma,linha,com,palavras,separadas,por,vírgula,e,determina,o," + \
        "comprimento,da,maior,palavra."
    palavras = separa(txt, ",")
    print(tam_maior_palavra(palavras))


main()
