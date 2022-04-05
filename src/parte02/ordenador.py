class Ordenador:

    def __init__(self, lista):
        self.lista = lista

    def sort_selection(self):
        lista = self.lista

        n_lista = len(lista)
        for i in range(n_lista - 1):
            i_menor = i
            for j in range(i + 1, n_lista):
                if lista[j] < lista[i_menor]:
                    i_menor = j
            lista[i], lista[i_menor] = lista[i_menor], lista[i]
        return lista

    def buble_sort(self):
        lista = self.lista
        n_lista = len(lista)
        for i in range(n_lista - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    def short_buble_sort(self):
        lista = self.lista
        n_lista = len(lista)
        for i in range(n_lista - 1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocou = True
            if not trocou:
                return lista
        return lista


if __name__ == "__main__":
    lst = [36, -40, 29, 16, 27, -22, 1, -41, 10, 1]
    print(lst)
    sorted_list = Ordenador(lst).sort_selection()
    print(sorted_list)
    sorted_list = Ordenador(lst).short_buble_sort()
    print(sorted_list)
