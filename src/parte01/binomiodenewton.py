def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


def coefNewton(n, k):
    c = fatorial(n) / (fatorial(k)*fatorial(n-k))
    return c


n0 = int(input("Expoente: "))
i = 0
while i <= n0:
    print(coefNewton(n0, i))
    i += 1
