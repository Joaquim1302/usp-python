"""Módulo com funções variadas"""
import random
import time


class Relogio:

    def __init__(self):
        self.time_begin = 0.0
        self.time_end = 0.0

    def cronometro_on(self):
        self.time_begin = time.time()

    def cronometro_off(self):
        if self.time_begin > 0:
            self.time_end = time.time()
        return self.time_end - self.time_begin

    def __str__(self):
        return f"{self.cronometro_off():5.3f}s"


class Parte02:

    def fibo(self, n):
        """Retorna uma série de Fibonacci até um número n"""
        resultado = [0]
        a, b = 0, 1
        while b < n:
            resultado.append(b)
            a, b = b, a+b
        return resultado

    def cria_lista(self, n):
        """Cria uma lista de n inteiros aleatórios"""
        lista = [random.randint(-50, 50) for _ in range(n)]
        return lista


if __name__ == "__main__":
    fibo_lst = Parte02().fibo(20)
    print(fibo_lst)

    random_lst = Parte02().cria_lista(10)
    print(random_lst)

    crono = Relogio()
    crono.cronometro_on()
    _ = input("Enter")
    _ = crono.cronometro_off()
    print(crono)
