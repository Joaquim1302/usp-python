import teste
import inc_dec  # The code to test


def test_increment():
    assert inc_dec.increment(3) == 4


def test_decrement():
    assert inc_dec.decrement(3) == 2


def test_minimo_int_list():
    assert teste.minimo_int_list([0]) == 0
    assert teste.minimo_int_list([-1, 0, 0, 0]) == -1
    assert teste.minimo_int_list([0, 1, 3, 10, -1]) == -1
    assert teste.minimo_int_list(
        [-5, 10, 15, 25, 30, 35, 10, 20, -10, 8]) == -10


def test_maximo_int_list():
    assert teste.maximo_int_list([0]) == 0
    assert teste.maximo_int_list([0, 0, 0, 0]) == 0
    assert teste.maximo_int_list([0, 1, 3, 10, -1]) == 10
    assert teste.maximo_int_list(
        [-5, 10, 15, 25, 30, 35, 10, 20, -10, 8]) == 35
