def encontra_impares(lista):
    if len(lista) == 0:
        return []
    num = lista.pop(0)
    if num % 2 != 0:
        return [num] + encontra_impares(lista)
    return encontra_impares(lista)


# a = [-1, 2, 3, 4, 5, 8]

# print(encontra_impares(a))
