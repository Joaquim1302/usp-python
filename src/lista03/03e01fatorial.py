# n = int(input("Digite o valor de n: "))


# def fatorial(n):
#     i = 1
#     fat = 1
#     while i <= n:
#         fat *= i
#         i += 1
#     return fat


def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


print(fatorial(0))
print(fatorial(1))
print(fatorial(2))
print(fatorial(3))
print(fatorial(4))
print(fatorial(5))
print(fatorial(8))
