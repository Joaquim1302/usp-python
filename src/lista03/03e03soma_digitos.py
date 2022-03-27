n = int(input("Digite o valor de n: "))

j = n
soma = 0
while j > 0:
    i = j % 10
    soma += i
    j //= 10
print(soma)
