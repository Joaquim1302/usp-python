class Complexo:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a != 0:
            s_complex = str(self.a)
        else:
            s_complex = ""

        if abs(self.b) == 1:
            s_b = "i"
        else:
            s_b = str(abs(self.b)) + "i"

        if self.b > 0:
            if self.a != 0:
                s_complex += " + "
            s_complex += s_b
        elif self.b < 0:
            s_complex += " - " + s_b
        return s_complex

    def imprima(self):
        print(self)

    def soma(self, complexo):
        self.a += complexo.a
        self.b += complexo.b

    def mult(self, complexo):
        self.a *= complexo.a
        self.b *= complexo.b


if __name__ == "__main__":
    z1 = Complexo(1, 1)
    z2 = Complexo(4, 5)
    print("z1 =", z1)
    print("z2 =", z2)
    z1.soma(z2)
    print("z1 + z2 =", z1)
    z2.mult(z2)
    print("z2 x z2 =", z2)
