print("Entre com o polinômio (x + b)^n")
# b = int(input("Segundo termo (valor)): "))
# n = int(input("Expoente: "))


def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


def coefNewton(n, k):
    c = fatorial(n) / (fatorial(k)*fatorial(n-k))
    return c


n = 10
i = 0
while i <= n:
    print(coefNewton(n, i))
    i += 1
