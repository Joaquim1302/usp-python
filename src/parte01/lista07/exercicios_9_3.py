def remove_repetidos(lst):
    new_lst = []
    for n in lst:
        if n not in new_lst:
            new_lst.append(n)
    new_lst.sort()
    return new_lst


def main():
    primos = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
              67, 71, 73, 79, 83, 89, 97]

    n = 10
    primos_p1 = primos[0:n]
    primos_p2 = primos[n - 5:n + 5]

    print(primos_p1)
    print(primos_p2)

    primos = primos_p2 + primos_p1
    print(primos)

    print(remove_repetidos(primos))


main()
