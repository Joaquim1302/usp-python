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


print(separa("recebe  um  string texto", " "))
