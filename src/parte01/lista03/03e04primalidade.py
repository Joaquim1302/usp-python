n = int(input("Digite um número inteiro: "))

i = 2
notPrimo = True
while i < n and notPrimo:
    if n % i == 0:
        notPrimo = False
        print("não primo")
    i += 1
if notPrimo:
    print("primo")
