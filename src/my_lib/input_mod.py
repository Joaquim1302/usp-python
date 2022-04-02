def input_int(msg, minimo, maximo, valor_default, msg_err):
    """Le um inteiro com msg de promt, valor entre minimo e máximo,
    um valor_default e uma mensagem de retorno para um enventual
    erro de leitura"""

    while True:
        try:
            n = int(input(msg) or valor_default)
            if not minimo <= n <= maximo:
                raise ValueError(msg_err)
        except ValueError as e:
            print(e)
        else:
            break
    return n


def input_float(msg, minimo, maximo, valor_default, msg_err):
    """Le um float com msg de promt, valor entre minimo e maximo,
    um valor_default e uma mensagem de retorno para um enventual
    erro de leitura"""
    while True:
        try:
            x = float(input(msg) or valor_default)
            if not minimo <= x <= maximo:
                raise ValueError(msg_err)
        except ValueError as e:
            print(e)
        else:
            break
    return x
