class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        a = self.a
        b = self.b
        c = self.c
        if (a < b + c) and (b < a + c) and (c < a + b):
            if (a == b) and (b == c):
                return "equilátero"
            elif (a == b) or (a == c):
                return "isóceles"
            else:
                return "escaleno"
        else:
            return "não é triângulo"

    def ordena_lados(self):
        a = self.a
        b = self.b
        c = self.c
        if a < b:
            a, b = b, a
        if b < c:
            b, c = c, b
        if a < b:
            a, b = b, a

        return a, b, c

    def retangulo(self):
        a, b, c = self.ordena_lados()
        return a ** 2 == b ** 2 + c ** 2

    def semelhantes(self, triangulo):
        t_1 = self.ordena_lados()
        t_2 = triangulo.ordena_lados()
        eh_semelhante = t_1[0] / t_2[0] == t_1[1] / t_2[1] == t_1[2] / t_2[2]
        return eh_semelhante


if __name__ == "__main__":
    t1 = Triangulo(2, 3, 5)
    t2 = Triangulo(4, 6, 10)
    print(t1.semelhantes(t2))

    t1 = Triangulo(2, 3, 5)
    t2 = Triangulo(4, 6, 15)
    print(t1.semelhantes(t2))
