class Fatorial:
    def calc_fatorial(self, n):
        """calcula o fatorial de de um número"""
        fat = 1
        while n > 1:
            fat *= n
            n -= 1
        return fat


if __name__ == "__main__":
    fat_obj = Fatorial()
    print(fat_obj.calc_fatorial(5))
