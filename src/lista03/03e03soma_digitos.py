n = int(input("Digite o valor de n: "))

j = n
sum = 0
while j > 0:
    i = j % 10
    sum += i
    j //= 10
print(sum)
