def fatorial(n):
    """calcula o fatorial de de um número"""
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


f = fatorial
