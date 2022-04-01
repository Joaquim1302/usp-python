def remove_repetidos(lst):
    new_lst = []
    for n in lst:
        if n not in new_lst:
            new_lst.append(n)
    new_lst.sort()
    return new_lst


# lista = [2, 4, 2, 2, 3, 3, 1]
# lista = remove_repetidos(lista)
# print(lista)

# lista = remove_repetidos([1, 2, 3, 3, 3, 4])
# print(lista)
