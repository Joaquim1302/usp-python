import pytest
import fatorial


class Testafatorial(fatorial.Fatorial):
    @pytest.mark.parametrize(
        "test_input,expected",
        [(0, 1), (1, 1), (10, 3628800), (4, 24), (5, 120), (-10, 1)])
    def test_fatorial(self, test_input, expected):
        assert self.calc_fatorial(test_input) == expected
