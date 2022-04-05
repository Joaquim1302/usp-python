import random


def cria_lista(n):
    lista = []
    for _ in range(n):
        lista.append(random.randint(-50, 50))
    return lista


def ordenada(lista):
    n_num = len(lista)
    if n_num < 3:
        return True
    if lista[0] < lista[1]:
        i = 0
        while i < n_num - 1:
            if not lista[i] < lista[i + 1]:
                return False
            i += 1
    else:
        i = 0
        while i < n_num - 1:
            if not(lista[i] > lista[i + 1]):
                return False
            i += 1
    return True


if __name__ == "__main__":

    lista1 = cria_lista(10)
    print(lista1, end=": ")
    print(ordenada(lista1))

    lista1 = [2, 4, 5, 6, 7, 8, 10, 13, 15, 16]
    print(lista1, end=": ")
    print(ordenada(lista1))

    lista1 = [16, 15, 13, 11, 10, 8, 6, 5, 4, 1]
    print(lista1, end=": ")
    print(ordenada(lista1))

    lista1 = [5, 4, 1]
    print(lista1, end=": ")
    print(ordenada(lista1))

    lista1 = [0, 12, 11]
    print(lista1, end=": ")
    print(ordenada(lista1))

    lista1 = [5, 3]
    print(lista1, end=": ")
    print(ordenada(lista1))

    lista1 = [0]
    print(lista1, end=": ")
    print(ordenada(lista1))
