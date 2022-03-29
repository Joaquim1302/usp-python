from re import I


def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


def combinacoes(n, m):
    if m < n:
        return " \n#Erro: o segundo número deve ser maior que o primeiro"
    comb = fatorial(m) / (fatorial(m-n) * fatorial(n))
    return comb


n = 12
m = 26
print("Combinação de", m, ",", n, "a", n, "=", combinacoes(n, m))
