
# def main():


# if __name__ == "__main__":
#     main()

def busca_binaria(lista, elemento, start=0, end=None):
    if end is None:
        end = len(lista)-1

    if end < start:
        return False
    else:
        meio = start + (end-start)//2

    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, start, meio - 1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio + 1, end)
    else:
        return meio


a = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]

print(busca_binaria(a, 99))


# def x(n):
#     if n >= 0 and n <= 2:
#         return n
#     else:
#         return x(n-1) + x(n-2) + x(n-3)


# print(x(6))
