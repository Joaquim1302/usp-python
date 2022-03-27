n = int(input("Digite um número inteiro: "))

i = n
while i // 10 != 0:
    j = (i % 100) // 10
    k = i % 10
    if j == k:
        print("sim")
        break
    i //= 10
if n < 10 or j != k:
    print("não")
