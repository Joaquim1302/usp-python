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


def le_arquivo(f_name):
    with open(f_name, 'r', encoding='utf-8') as arq_entrada:
        conteudo = arq_entrada.read()

    return conteudo


def soma_elementos(lst):
    soma = 0.0
    for n in lst:
        soma += float(n)
    return soma


def main():
    text = le_arquivo("D:\\Trash\\cursos\\exerc_13_3_le_arquivo.txt")
    linhas = separa(text, "\n")
    tt_linhas = 0.0
    for linha in linhas:
        linha = separa(linha, " ")
        sub_tt_linhas = soma_elementos(linha)
        print("Soma =", f"{sub_tt_linhas: 9.6f}")
        tt_linhas += sub_tt_linhas
    print("tt_linhas =", f"{tt_linhas: 9.6f}")


if __name__ == "__main__":
    main()
