import pytest
import fatorial_rec
import fibo_rec
import binary_search_rec


@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])
def test_fatorial_rec(entrada, esperado):
    assert fatorial_rec.fat_rec(entrada) == esperado


@pytest.mark.parametrize("entrada, esperado", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13)
])
def test_fibo_rec(entrada, esperado):
    assert fibo_rec.fibo_rec(entrada) == esperado


a = [10, 20, 30, 40, 50, 60]


@pytest.mark.parametrize("lista, valor, esperado", [
    (a, 60, 5),
    (a, 30, 2),
    (a, 50, 4),
    (a, 70, False),
    (a, 15, False),
    (a, 10, 0)])
def test_binary_search_recursive(lista, valor, esperado):
    assert binary_search_rec.binary_search_recursive(lista, valor) == esperado
