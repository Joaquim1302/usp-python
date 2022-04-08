def merge_sort_ultra_rec_rec(lst):
    """Ordena a lista lst"""
    print("Splitting ", lst)
    if len(lst) > 1:
        mid = len(lst) // 2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]

        merge_sort_ultra_rec_rec(lefthalf)
        merge_sort_ultra_rec_rec(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k] = lefthalf[i]
                i = i + 1
            else:
                lst[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            lst[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            lst[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", lst)


def merge_sort_ultra_rec(lst):
    """Retorna uma lista ordenada lst"""
    if len(lst) <= 1:  # base da recursão
        return lst

    mid = len(lst) // 2

    lefthalf = merge_sort_ultra_rec(lst[:mid])
    righthalf = merge_sort_ultra_rec(lst[mid:])

    return merge(lefthalf, righthalf)


def merge(lefthalf, righthalf):
    if not lefthalf:  # base
        return righthalf

    if not righthalf:  # base
        return lefthalf

    if lefthalf[0] < righthalf[0]:
        return [lefthalf[0]] + merge(lefthalf[1:], righthalf)

    return [righthalf[0]] + merge(lefthalf, righthalf[1:])


if __name__ == "__main__":
    print("Merge recursiva")
    lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort_ultra_rec_rec(lista)
    print(lista)

    print("Merge ultra recursiva")
    lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    lst = merge_sort_ultra_rec(lista)
    print(lst)
