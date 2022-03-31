def minimo_int_list(int_list):
    i = 0
    minimo = int_list[0]
    while i < len(int_list):
        if int_list[i] < minimo:
            minimo = int_list[i]
        i += 1
    return minimo


def maximo_int_list(int_list):
    i = 0
    maximo = int_list[0]
    while i < len(int_list):
        if int_list[i] > maximo:
            maximo = int_list[i]
        i += 1
    return maximo


temps = [-5, 10, 15, 25, 30, 35, 10, 20, -10, 8]
print(f'mínima {minimo_int_list(temps):3d} Cº')
print(f'máxima {maximo_int_list(temps):3d} Cº')
