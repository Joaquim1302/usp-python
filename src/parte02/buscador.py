class Buscador:

    def __init__(self, lista):
        self.lista = lista

    def seq_search(self, item):
        """Busca sequencial"""
        lista = self.lista

        pos = 0
        found = False
        while pos < len(lista) and not found:
            if lista[pos] == item:
                found = True
            else:
                pos += 1
        return found

    def binary_search(self, item):
        """Busca binária"""
        lista = self.lista

        first = 0
        last = len(lista) - 1
        found = False
        while first <= last and not found:
            midpoint = (first + last) // 2
            if lista[midpoint] == item:
                found = True
            else:
                if item < lista[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return found


if __name__ == "__main__":
    lst = [-100, 0, 20, 30, 50, 100, 3000, 5000]
    print(Buscador(lst).seq_search(3))
    print(Buscador(lst).seq_search(0))
    print("--------------")
    print(Buscador(lst).seq_search(100))
    print(Buscador(lst).seq_search(0))
    print(Buscador(lst).seq_search(-1000))
    print(Buscador(lst).seq_search(5000))
    print(Buscador(lst).seq_search(7000))
    print(Buscador(lst).seq_search(70))
