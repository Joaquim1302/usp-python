def fibonacci(n):
    """Retorna uma série de Fibonacci até um número n"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# if __name__ == "__main__":
#     print(fibonacci(4))
#     print(fibonacci(2))
