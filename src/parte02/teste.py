import random
from os import system, name
import mod_teste


def clear():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


# from mod_input import fibo, mensagem
# mensagem()
# print(fibo(random.randint(1, 100)))
# melhor evitar sintaxe acima para evitar criar/chamar funções de mesmo nome
mod_teste.mensagem()
print(mod_teste.fibo(random.randint(1, 100)))

clear()

for i in range(8):
    for j in range(8):
        print(f"[{i:1d},{j:1d}];", end="")
    print()


# s = "Naze"
# l = list(s)
# l[2] = 'm'
# s = "".join(l)
# print(s)


def replace_char(word, c, pos):
    if isinstance(word, list):
        l_word = list(word[0])
    if isinstance(word, str):
        l_word = list(word)
    l_word[pos] = c
    word = "".join(l_word)
    return word


print(replace_char("word", "X", 2))
print(type(replace_char("word", "X", 2)))
print(replace_char(["word"], "Y", 1))
print(type(replace_char(["word"], "X", 2)))

# def main():


# if __name__ == "__main__":
#     main()
