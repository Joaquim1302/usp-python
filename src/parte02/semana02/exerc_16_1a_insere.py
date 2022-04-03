def insere_se_novo(nome, lista):
    ''' (str, list) -> int
        modifica a lista, inserindo nome na lista.
        Retorna a posição de nome na lista ou None caso ele já exista.
    '''
    if lista.count(nome) > 0:
        for i, nom_s in enumerate(lista):
            if nom_s == nome:
                return i
    else:
        lista.append(nome)
        return len(lista)-1


def main():
    lista = ["Ronaldo", "Romario", "Rivelino"]
    pos = insere_se_novo("Romario", lista)
    print(pos)
    pos = insere_se_novo("Pele", lista)
    print(pos)
    pos = insere_se_novo("Rivelino", lista)
    print(pos)
    print(lista, " que deve ser Ronaldo, Romario, Rivelino, Pele")


if __name__ == "__main__":
    main()
