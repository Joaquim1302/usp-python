import fatorial


def test_fatorial0():
    assert fatorial.fatorial(0) == 1


def test_fatorial1():
    assert fatorial.fatorial(1) == 1


def test_fatorial_negativo():
    assert fatorial.fatorial(10) == 3628800


def test_fatorial4():
    assert fatorial.fatorial(4) == 24


def test_fatorial5():
    assert fatorial.fatorial(5) == 120
