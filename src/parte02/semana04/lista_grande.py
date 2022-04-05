import random


def cria_lista(n):
    lista = [0 for _ in range(n)]
    for i in range(n):
        lista[i] = random.randint(-50, 50)
    return lista


if __name__ == "__main__":

    lista1 = cria_lista(10)
    print(lista1)
