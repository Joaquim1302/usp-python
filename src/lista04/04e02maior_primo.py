def ehPrimo(n):
    i = 2
    notPrimo = True
    while i < n and notPrimo:
        if n % i == 0:
            return False
        i += 1
    return True


def maior_primo(n):
    if n < 2:
        return "Não é maior ou igual a 2"
    i = n
    while i >= 2:
        if ehPrimo(i):
            return i
        i -= 1


# print(maior_primo(100))
# print(maior_primo(37))
# print(maior_primo(96))
# print(maior_primo(2))

n = int(input("Digite um número inteiro maior ou igual a 2: "))
print(maior_primo(n))
