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

    def retangulo(self):
        v_1 = self.a
        v_2 = self.b
        v_3 = self.c
        # identificar a hipotenusa
        if v_1 > v_2 and v_1 > v_3:
            hip = v_1
            a = v_2
            b = v_3
        elif v_2 > v_1 and v_2 > v_3:
            hip = v_2
            a = v_1
            b = v_3
        else:
            hip = v_3
            a = v_1
            b = v_2

        return hip ** 2 == a ** 2 + b ** 2


if __name__ == "__main__":
    t = Triangulo(1, 3, 5)
    print(t.retangulo())

    u = Triangulo(5, 3, 4)
    print(u.retangulo())
