from os import system, name


def clear():

    if name == 'nt':
        _ = system('cls')  # windows

    else:
        _ = system('clear')  # os


def init_tab():

    tabuleiro = [
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        "]
    return tabuleiro


def replace_char(word, c, pos):
    if isinstance(word, list):
        l_word = list(word[0])
    if isinstance(word, str):
        l_word = list(word)
    l_word[pos] = c
    word = "".join(l_word)
    return word


def poe_peca(tabuleiro, ds_peca, i, j):
    tabuleiro[i] = replace_char(tabuleiro[i], ds_peca, j)
    return tabuleiro


def tira_peca(tabuleiro, i, j):
    tabuleiro[i] = replace_char(tabuleiro[i], " ", j)
    return tabuleiro


def ataque_rainha(tabuleiro, lin, col):
    # coluna
    for i in range(8):
        if i != lin:
            poe_peca(tabuleiro, "X", i, col)

    # linha
    for j in range(8):
        if j != col:
            poe_peca(tabuleiro, "X", lin, j)

    # pra esquerda pra cima
    i = lin - 1
    j = col - 1
    while j >= 0 and i >= 0:
        poe_peca(tabuleiro, "X", i, j)
        j -= 1
        i -= 1

    # pra  direita pra cima
    i = lin - 1
    j = col + 1
    while i >= 0 and j < 8:
        poe_peca(tabuleiro, "X", i, j)
        j += 1
        i -= 1

    # pra esquerda pra baixo
    i = lin + 1
    j = col - 1
    while j >= 0 and i < 8:
        poe_peca(tabuleiro, "X", i, j)
        j -= 1
        i += 1

    # pra direita pra baixo
    i = lin + 1
    j = col + 1
    while i < 8 and j < 8:
        poe_peca(tabuleiro, "X", i, j)
        j += 1
        i += 1
    return tabuleiro


def marque_atacadas(tabuleiro, peca, i, j):
    match peca:
        case "R":
            tabuleiro = ataque_rainha(tabuleiro, i, j)
            return tabuleiro
        case "P":
            return tabuleiro
        case "C":
            return tabuleiro


def print_tabuleiro(tabuleiro, i, j, str_parar):
    clear()
    print("+---+---+---+---+---+---+---+---+")
    for lin in tabuleiro:
        linha = list(lin)
        for k in range(8):
            print(f"| {linha[k]} ", end="")
        print("|")
        print("+---+---+---+---+---+---+---+---+")
    print(f"[{i:1d},{j:1d}]")
    if str_parar == "parar":
        _ = input("[Enter] para continuar")


def posicao(tabuleiro, i, j):
    poe_peca(tabuleiro, "R", i, j)
    print_tabuleiro(tabuleiro, i, j, "não parar")

    marque_atacadas(tabuleiro, "R", i, j)
    print_tabuleiro(tabuleiro, i, j, "parar")


def main():

    tabuleiro = init_tab()
    posicao(tabuleiro, 4, 3)

    tabuleiro = init_tab()
    posicao(tabuleiro, 0, 0)

    tabuleiro = init_tab()
    posicao(tabuleiro, 7, 7)

    tabuleiro = init_tab()
    posicao(tabuleiro, 5, 6)

    tabuleiro = init_tab()
    posicao(tabuleiro, 3, 6)


if __name__ == "__main__":
    main()
