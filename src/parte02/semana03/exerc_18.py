def mdc(a, b):
    """máximo divisor comum"""
    # algoritmo de Euclides iterativo
    while b != 0:
        resto = a % b
        a, b = b, resto
    return a


class Racional:
    def __init__(self, num=0, den=1):
        self.put(num, den)

    def __str__(self):
        num = int(round(self.num, 1))
        den = int(round(self.den, 1))
        return f"{num}/{den}"

    def get(self):
        return self.num, self.den

    def put(self, num=0, den=1):
        self.num, self.den = num, den

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Racional(num, den)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return Racional(num, den)

    def mdc(self, other):
        """máximo divisor comum"""
        # algoritmo de Euclides iterativo
        a = self.den
        b = other.den
        # while b != 0:
        #     resto = a % b
        #     a, b = b, resto
        a = mdc(a, b)
        return a

    def mmc(self, other):
        """mínimo múltiplo comum"""
        a = self.den
        b = other.den
        return a * (b / self.mdc(other))

    def __add__(self, other):
        """Soma duas frações"""
        mmc = self.mmc(other)
        num = mmc * ((self.num / self.den) + (other.num / other.den))
        return Racional(num, mmc)

    def __sub__(self, other):
        """Subtrai duas frações"""
        mmc = self.mmc(other)
        num = mmc * ((self.num / self.den) - (other.num / other.den))
        return Racional(num, mmc)

    def rdc(self):
        """Reduz uma fração"""
        a = self.num
        b = self.den
        mindc = mdc(a, b)
        a /= mindc
        b /= mindc
        return Racional(a, b)


if __name__ == "__main__":
    r1 = Racional(2, 5)
    r2 = Racional(1, 2)
    print(r1, '*', r2, '=>', r1 * r2)
    print(r1, '/', r2, '=>', r1 / r2)
    # print("mdc de", r1, 'e', r2, '=>', r1.mdc(r2))
    # print("mmc de", r1, 'e', r2, '=>', r1.mmc(r2))
    print(r1, '+', r2, '=>', r1 + r2)
    print(r1, '-', r2, '=>', r1 - r2)
    r3 = Racional(4, 18)
    print(r3, '=>', r3.rdc())
