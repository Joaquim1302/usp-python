def main():
    n = int(input("Digite n: "))
    i = int(input("Digite i: "))
    j = int(input("Digite j: "))

    # mutiplos de i e j
    mult_i = mult_j = 0

    k = 0
    while k < n:
        if mult_i == mult_j:
            print(mult_i)
            mult_i = mult_i + i
            mult_j = mult_j + j
        elif mult_i < mult_j:
            print(mult_i)
            mult_i = mult_i + i
        else:
            print(mult_j)
            mult_j = mult_j + j

        k = k + 1


# -------------------------------------------------
main()
