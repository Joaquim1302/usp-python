"""Módulo com funções variadas"""


def fibo(n):
    """Retorna uma série de Fibonacci até um número n"""
    resultado = [0]
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado


def mensagem():
    print("Teste de módulo")


if __name__ == "__main__":
    print("Está rodando como principal")
    print(fibo(20))
