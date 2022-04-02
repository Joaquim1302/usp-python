def menor_nome(nomes):
    menor = nomes[0].strip().capitalize()
    c_menor = len(menor)
    for nome in nomes:
        nome = nome.strip().capitalize()
        if len(nome) < c_menor:
            c_menor = len(nome)
            menor = nome
    return menor


# print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))
# print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))
# print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']))
# print(menor_nome(['LU   ', ' josé ', 'PAULO', 'Catarina']))
# print(menor_nome(['zé', ' lu', 'fê']))
