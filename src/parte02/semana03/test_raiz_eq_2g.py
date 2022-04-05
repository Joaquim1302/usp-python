import pytest
import raiz_eq_2g


class Testbaskara(raiz_eq_2g.Bhaskara):
    @pytest.mark.parametrize("entrada, esperado", [
        ((1, 0, 0), (1, 0)),
        ((1, -5, 6), (2, 3, 2)),
        ((10, 10, 10), (0)),
        ((10, 20, 10), (1, -1))
    ])
    def test_bhaskara(self, entrada, esperado):
        assert self.calcula_eq_2g(
            entrada[0], entrada[1], entrada[2]) == (esperado)
