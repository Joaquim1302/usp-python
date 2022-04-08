def fibo_rec(n):
    """Retorna uma série de Fibonacci até um número n"""
    if n < 2:
        return n
    return fibo_rec(n - 1) + fibo_rec(n - 2)
