import ordenador
import mod_parte02
import buscador


class TestaOrdenador:

    def is_sorted(self, lista):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                return False
        return True

    def test_short_buble_sort(self):
        lista = mod_parte02.Parte02().cria_lista(1000)
        sorted_list = ordenador.Ordenador(lista).short_buble_sort()
        assert self.is_sorted(sorted_list)

    def test_sort_selection(self):
        lista = mod_parte02.Parte02().cria_lista(1000)
        sorted_list = ordenador.Ordenador(lista).sort_selection()
        assert self.is_sorted(sorted_list)

    def test_buble_sort(self):
        lista = mod_parte02.Parte02().cria_lista(1000)
        sorted_list = ordenador.Ordenador(lista).buble_sort()
        assert self.is_sorted(sorted_list)

    def test_insertion_sort(self):
        lista = mod_parte02.Parte02().cria_lista(1000)
        sorted_list = ordenador.Ordenador(lista).insertion_sort()
        assert self.is_sorted(sorted_list)


class TestaBuscador:

    def cria_lista(self):
        lst = mod_parte02.Parte02().cria_lista(1000)
        return ordenador.Ordenador(lst).buble_sort()

    def test_seq_search(self):
        lst = self.cria_lista()
        num = lst[100]
        assert buscador.Buscador(lst).seq_search(num)

    def test_binary_search(self):
        lst = self.cria_lista()
        num = lst[99]
        assert buscador.Buscador(lst).binary_search(num)
