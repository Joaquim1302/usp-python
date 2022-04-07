def bubble_sort(lista):
    n_lista = len(lista)
    for i in range(n_lista - 1, 0, -1):
        trocou = False
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
                trocou = True
        if not trocou:
            return lista
    return lista


# if __name__ == "__main__":
#     print(bubble_sort([1, 5, 3, 4, 2, 0]))
