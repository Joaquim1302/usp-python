from math import sqrt


class Bhaskara:

    def calcula_eq_2g(self, a, b, c):
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return 0
        elif delta == 0:
            x_1 = -b / (2*a)
            return 1, x_1
        else:
            dlt = sqrt(delta)
            x_1 = (-b + dlt) / (2*a)
            x_2 = (-b - dlt) / (2*a)
            return 2, x_1, x_2

    def main(self):
        a_1 = float(input("a: "))
        b_1 = float(input("b: "))
        c_1 = float(input("c: "))
        raizes = self.calcula_eq_2g(a_1, b_1, c_1)
        if raizes == 0:
            print('Não existem raízes reais para a equação')
        elif raizes[0] == 1:
            print(f'uma raíz \n x={raizes[1]:7.2}')
        elif raizes[0] == 2:
            print(
                f'duas raízes \n x1={raizes[1]:7.2} \n x2={raizes[2]:7.2}')

#  x2 + x + 1 { , }
#  x2 - 5x + 6 {3, 2}
# 4x2 - 4x + 1 {0.5, 0.5}
#  x2 + 2x - 15 {3, -5}


if __name__ == "__main__":
    # main()
    obj_bsk = Bhaskara()
    # b.main()

    print(obj_bsk.calcula_eq_2g(10, -20, 5))
