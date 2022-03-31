import re


def textos_para_teste():
    textos = []
    textos.append("Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.")
    textos.append("Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.")
    textos.append("Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens.")

    return textos


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


# ---------------------------------------------------

def remove_pontuacao(texto):
    return re.sub(r'[^\w\s]', '', texto)


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
    sal = 0.0
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
        sim += (as_a[i] - as_b[i])
        i += 1
    sim /= 6
    return sim


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura
    ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade
    de ter sido infectado por COH-PIAH.'''
    print(ass_cp)

    similaridade = 0
    i = 0
    n_textos = len(textos)
    while i < n_textos:
        sim = compara_assinatura(calcula_assinatura(textos[i]), ass_cp)
        if sim > similaridade:
            similaridade = sim
            infectado = i
        i += 1
    return infectado


def main():
    # le assinatura a ser comparada com os textos fornecidos
    ass_cp = le_assinatura()

    # le os textos
    # textos = le_textos()

    #  SOMENTE PARA TESTES. DEVE SER SUBSTITUIDO PELA LINHA ACIMA
    textos = textos_para_teste()

    # recebe uma lista de textos e uma assinatura e devolve qual texto com
    # maior probabilidade de ter sido infectado por COH-PIAH
    avalia_textos(textos, ass_cp)

    # recebe um texto e devolve a assinatura do texto
    # print(calcula_assinatura(texto))


main()
