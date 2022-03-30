def ehPrimo(n):
    i = 2
    notPrimo = True
    while i < n and notPrimo:
        if n % i == 0:
            return False
        i += 1
    return True


def n_primos(n0):
    count = 0
    i = 2
    while i <= n0:
        if ehPrimo(i):
            print(i, end=", ")
            count += 1
        i += 1
    return count


n_primos(100)
