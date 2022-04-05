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


# if __name__ == "__main__":
#     t = Triangulo(4, 4, 4)
#     print(t.tipo_lado())

#     u = Triangulo(3, 4, 5)
#     print(u.tipo_lado())

#     u = Triangulo(4, 4, 5)
#     print(u.tipo_lado())

#     u = Triangulo(10, 4, 5)
#     print(u.tipo_lado())
