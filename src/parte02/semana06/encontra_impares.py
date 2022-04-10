def encontra_impares(lista):
    """Retorna lista com os números ímpares"""
    if len(lista) == 0:
        return []
    imp = lista.pop(0)
    if imp % 2 != 0:
        return [imp] + encontra_impares(lista)
    return encontra_impares(lista)


# if __name__ == "__main__":
#     a = [-1, 2, 3, 4, 7, 16, 17]
#     print(encontra_impares(a))
