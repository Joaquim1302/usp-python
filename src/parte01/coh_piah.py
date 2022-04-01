import re


def input_float(msg, minimo, maximo, msg_err):
    while True:
        try:
            x = float(input(msg))
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

    wal = float(input_float(
        "Entre o tamanho médio de palavra: ", 0.0, 1000.0,  ""))
    ttr = float(input_float(
        "Entre a relação Type-Token: ", 0.0, 100.0,  ""))
    hlr = float(input_float(
        "Entre a Razão Hapax Legomana: ", 0.0, 100.0,  ""))
    sal = float(input_float(
        "Entre o tamanho médio de sentença: ", 0.0, 10000.0,  ""))
    sac = float(input_float(
        "Entre a complexidade média da sentença: ", 0.0, 100.0,  ""))
    pal = float(input_float(
        "Entre o tamanho medio de frase: ", 0.0, 1000.0,  ""))

    # print()
    # wal = 4.51
    # ttr = 0.693
    # hlr = 0.55
    # sal = 70.82
    # sac = 1.82
    # pal = 38.5

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


# ---------------------------------------------------

def remove_pontuacao(texto):
    return re.sub(r'\!|\'|\?|\.|\,|\:|\;', '', texto)
    # return re.sub(r'[^\w\s]', '', texto)


def tam_medio_palavras(lista_palavras, n_palavras):

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


def rel_hapax_legomana(lista_palavras, n_palavras):
    hlr = n_palavras_unicas(lista_palavras) / n_palavras
    return hlr


def tam_medio_sentencas(sentencas):
    n_sentencas = len(sentencas)
    sal = 0
    i = 0
    while i < n_sentencas:
        sal += len(sentencas[i])
        i += 1
    sal /= n_sentencas
    return sal


def complex_sentencas(sentencas):
    n_sentencas = len(sentencas)
    i = 0
    sac = 0.0
    while i < n_sentencas:
        sac += len(separa_frases(sentencas[i]))
        i += 1
    sac /= n_sentencas
    return sac


def tam_medio_frases(sentencas):
    n_sentencas = len(sentencas)
    i = 0
    n_frases = 0
    pal = 0.0
    while i < n_sentencas:
        frases = separa_frases(sentencas[i])
        n_frases += len(frases)
        j = 0
        while j < len(frases):
            pal += len(frases[j])
            j += 1
        i += 1
    pal /= n_frases
    return pal


def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a
    assinatura do texto.'''
    lista_palavras = separa_palavras(remove_pontuacao(texto))
    # print(lista_palavras)
    n_palavras = len(lista_palavras)
    sentencas = separa_sentencas(texto)

    assinatura = []

    wal = tam_medio_palavras(lista_palavras, n_palavras)
    ttr = rel_type_token(lista_palavras, n_palavras)
    hlr = rel_hapax_legomana(lista_palavras, n_palavras)
    sal = tam_medio_sentencas(sentencas)
    sac = complex_sentencas(sentencas)
    pal = tam_medio_frases(sentencas)

    assinatura.append(wal)
    assinatura.append(ttr)
    assinatura.append(hlr)
    assinatura.append(sal)
    assinatura.append(sac)
    assinatura.append(pal)

    return assinatura


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve
    devolver o grau de similaridade nas assinaturas.
    as_b deve ser = ass_cp a assinatura conhecida'''
    sim = 0.0
    i = 0
    while i < 6:
        sim += abs(as_a[i] - as_b[i])
        i += 1
    sim /= 6
    return sim


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura
    ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade
    de ter sido infectado por COH-PIAH.'''
    similaridade = 10000
    i = 0
    n_textos = len(textos)
    while i < n_textos:
        sim = compara_assinatura(calcula_assinatura(textos[i]), ass_cp)
        if sim < similaridade:
            similaridade = sim
            infectado = i
        i += 1
    return infectado + 1


def main():

    # le assinatura a ser comparada com os textos fornecidos
    ass_cp = le_assinatura()

    #  SOMENTE PARA TESTES. DEVE SER SUBSTITUIDO PELA FUNÇÃO ABAIXO
    # textos = textos_para_teste()

    # le os textos
    textos = le_textos()

    # recebe uma lista de textos e uma assinatura e devolve qual texto com
    # maior probabilidade de ter sido infectado por COH-PIAH
    infectado = avalia_textos(textos, ass_cp)
    print("\nO autor do texto " + str(infectado) +
          " está infectado com COH-PIAH\n")


main()
