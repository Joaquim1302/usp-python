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

    def insertion_sort(self):
        lista = self.lista
        for index in range(1, len(lista)):
            currentvalue = lista[index]
            position = index
            while position > 0 and lista[position-1] > currentvalue:
                lista[position] = lista[position-1]
                position = position-1
            lista[position] = currentvalue
        return lista


if __name__ == "__main__":
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(lst)
    sorted_list = Ordenador(lst).buble_sort()
    print(sorted_list)
    sorted_list = Ordenador(lst).short_buble_sort()
    print(sorted_list)
    sorted_list = Ordenador(lst).insertion_sort()
    print(sorted_list)
