import ordenador
import mod_parte02


class TestaOrdenador:

    def is_sorted(self, lista):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                return False
        return True

    def test_short_buble_sort(self):
        lista = mod_parte02.Parte02().cria_lista(5)
        sorted_list = ordenador.Ordenador(lista).sort_selection()
        assert self.is_sorted(sorted_list)
