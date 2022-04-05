def ordena(lista):
    i = 0
    n_lista = len(lista)
    while i < n_lista:
        i_menor = i
        j = i + 1
        while j < n_lista:
            if lista[j] < lista[i_menor]:
                i_menor = j
            j += 1
        lista[i], lista[i_menor] = lista[i_menor], lista[i]
        i += 1


if __name__ == "__main__":
    lst = [36, -40, 29, 16, 27, -22, 1, -41, 10, 1]
    ordena(lst)
    print(lst)
