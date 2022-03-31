import re


# def input_int(msg, minimo, maximo, valor_default, msg_err):
#     while True:
#         try:
#             n = int(input(msg) or valor_default)
#             if not minimo <= n <= maximo:
#                 raise ValueError(msg_err)
#         except ValueError as e:
#             print(e)
#         else:
#             break
#     return n


def input_float(msg, minimo, maximo, valor_default, msg_err):
    while True:
        try:
            x = float(input(msg) or valor_default)
            if not minimo <= x <= maximo:
                raise ValueError(msg_err)
        except ValueError as e:
            print(e)
        else:
            break
    return x


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma
    assinatura a ser comparada com os textos fornecidos'''
    print("\nBem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:\n")

    wal = 4.51
    ttr = 0.693
    hlr = 0.55
    sal = 70.82
    sac = 1.82
    pal = 38.5

    # wal = float(input_float(
    #     "Entre o tamanho médio de palavra: ", 0.0, 100.0, wal, ""))
    # ttr = float(input_float(
    #     "Entre a relação Type-Token: ", 0.0, 100.0, ttr, ""))
    # hlr = float(input_float(
    #     "Entre a Razão Hapax Legomana: ", 0.0, 100.0, hlr, ""))
    # sal = float(input_float(
    #     "Entre o tamanho médio de sentença: ", 0.0, 100.0, sal, ""))
    # sac = float(input_float(
    #     "Entre a complexidade média da sentença: ", 0.0, 100.0, sac, ""))
    # pal = float(input_float(
    #     "Entre o tamanho medio de frase: ", 0.0, 100.0, pal, ""))
    print()
    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista
    contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do
    texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro
    da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro
    da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras
    que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de
    palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def tam_medio_palavra(lista_palavras, n_palavras):

    # print(lista_palavras)

    i = 0
    wal = 0.0
    while i < n_palavras:
        wal += len(lista_palavras[i])
        i += 1
    wal /= i
    return wal


def rel_type_token(lista_palavras, n_palavras):

    ttr = n_palavras_diferentes(lista_palavras) / n_palavras
    return ttr

    # def compara_assinatura(as_a, as_b):
    #     '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve
    #     devolver o grau de similaridade nas assinaturas.'''
    #     pass


def rel_hapax_legomana(lista_palavras, n_palavras):
    hlr = n_palavras_diferentes(lista_palavras) / n_palavras
    return hlr


def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a
    assinatura do texto.'''
    lista_palavras = separa_palavras(texto)
    n_palavras = len(lista_palavras)

    wal = tam_medio_palavra(lista_palavras, n_palavras)
    ttr = rel_type_token(lista_palavras, n_palavras)
    hlr = rel_hapax_legomana(lista_palavras, n_palavras)
    print(wal, ttr, hlr)


# def avalia_textos(textos, ass_cp):
#     '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura
#     ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade
#     de ter sido infectado por COH-PIAH.'''
#     pass


def remove_pontuacao(texto):
    return re.sub(r'[^\w\s]', '', texto)


def main():
    # texto = "Então resolveu ir brincar com a Máquina pra ser também " + \
    #     "imperador dos filhos da mandioca. Mas as três cunhas deram " + \
    #     "muitas risadas e falaram que isso de deuses era gorda mentira " + \
    #     "antiga, que não tinha deus não e que com a máquina ninguém " + \
    #     "não brinca porque ela mata. A máquina não era deus não, nem " + \
    #     "possuía os distintivos femininos de que o herói gostava tanto."
    texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."
    # le assinatura a ser comparada com os textos fornecidos
    le_assinatura()
    # recebe um texto e devolve a assinatura do texto
    calcula_assinatura(remove_pontuacao(texto))


main()
