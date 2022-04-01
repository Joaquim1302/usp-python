def fatorial(n):
    # Calcula o fatorial do número n
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


def eh_letra(c):
    ac = ord(c)
    a = (ac >= 65 and ac <= 90)
    b = (ac >= 97 and ac <= 122)
    c = a or b
    return c


def input_int(msg, minimo, maximo, msg_err):
    while True:
        try:
            n = int(input(msg))
            if not minimo <= n <= maximo:
                raise ValueError(msg_err)
        except ValueError as e:
            print(e)
        else:
            break
    return n


def mdc(a, b):
    """(int,int) -> int
    Recebe dois inteiros positivos a e b e retorna
    o seu maximo divisor comum.
    """

    m = a

    while a % m != 0 or b % m != 0:
        m -= 1

    return m


# def main():

#     # leia o tamanho da sequencia
#     n = int(input("Digite o tamanho da sequencia (>0): "))

#     mdc_atual = int(input("Digite o 1o. numero: "))
#     i = 1  # contador de numeros lidos
#     while i < n:
#         num = int(input("Digite o " + str(i+1) + "o. numero: "))
#         i = i + 1
#         mdc_atual = mdc(mdc_atual, num)

#     print("O mdc eh", mdc_atual)


# main()  # chamada da funcao principal

def minimo_int_list(int_list):
    i = 1
    minimo = int_list[0]
    while i < len(int_list):
        if int_list[i] < minimo:
            minimo = int_list[i]
        i += 1
    return minimo


def maximo_int_list(int_list):
    i = 1
    maximo = int_list[0]
    while i < len(int_list):
        if int_list[i] > maximo:
            maximo = int_list[i]
        i += 1
    return maximo
