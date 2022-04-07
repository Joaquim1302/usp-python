def busca(lista, elemento):
    """Busca binária"""
    first = 0
    last = len(lista) - 1
    while first <= last:
        midpoint = (first + last) // 2
        print(midpoint)
        if lista[midpoint] == elemento:
            return midpoint
        else:
            if elemento < lista[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return False


# if __name__ == "__main__":
#     print(busca(['a', 'e', 'i'], 'a'))
#     # print(busca([1, 2, 3, 4, 5], 6))
#     # print(busca([1, 2, 3, 4, 5, 6], 4))
