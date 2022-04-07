def insertion_sort(lista):
    for index in range(1, len(lista)):
        currentvalue = lista[index]
        position = index
        while position > 0 and lista[position-1] > currentvalue:
            lista[position] = lista[position-1]
            position = position-1
        lista[position] = currentvalue
    return lista


# if __name__ == "__main__":
#     print(insertion_sort([17, 20, 26, 31, 44, 54, 55, 77, 93]))
