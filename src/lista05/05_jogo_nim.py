JOGADOR = 1
COMPUTADOR = 2


def inputInt(msg, minimo, maximo, msgErr):
    while True:
        try:
            n = int(input(msg))
            if not (minimo <= n <= maximo):
                raise ValueError(msgErr)
        except ValueError as e:
            print(e)
        else:
            break
    return n


def quem_comeca(n, m):
    if (n % (m + 1)) == 0:
        print("Você começa!")
        return JOGADOR
    else:
        print("Computador começa!")
        return COMPUTADOR


def msgRetirada(j, p):
    jogadores = {1: "Você", 2: "O computador"}
    if p == 1:
        sP = " uma peça."
    else:
        sP = str(p) + " peças."
    msg = jogadores[j] + " tirou " + sP
    print(msg)


def printResta(n):
    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
    else:
        print("Agora restam", n, "peças no tabuleiro.")


def maxPc(n, m):
    if n < m:
        return n
    else:
        return m


def computador_escolhe_jogada(n, m):
    # Estratégia vencedora: deixar sempre múltiplos de (m+1)
    # peças ao jogador oponente
    if n <= m:
        pecas = n  # tira as restantes e ganha o jogo
    else:
        # o valor resultante de n nenos o resto da divisão
        # por (m -1) é um multiplo de n
        pecas = n % (m + 1)
        if pecas == 0:
            pecas = m
    if pecas > 0:
        msgRetirada(COMPUTADOR, pecas)
        return pecas
    msgRetirada(COMPUTADOR, pecas)
    return pecas


def usuario_escolhe_jogada(n, m):
    pecas = inputInt("Quantas peças você vai tirar? ", 1, maxPc(n, m),
                     "Oops! Jogada inválida! Tente de novo.\n")
    msgRetirada(JOGADOR, pecas)
    return pecas


def partida():
    n = inputInt("Quantas peças? ", 2, 100, "Escolha entre 2 e 100 peças")
    m = inputInt("Limite de peças por jogada? ", 1,
                 n - 1, "Escolha entre 1 e " + str(n - 1) + " peças")

    jogador = quem_comeca(n, m)
    while n > 0:
        if jogador == COMPUTADOR:
            pecas = computador_escolhe_jogada(n, m)
        else:
            pecas = usuario_escolhe_jogada(n, m)
        n -= pecas
        printResta(n)
        jogador = 3 - jogador

    if jogador == COMPUTADOR:
        print("Fim do jogo! O computador ganhou!")
    else:
        print("Fim do jogo! Você ganhou!")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada\n")
    eh_campeonato = inputInt(
        "2 - para jogar um campeonato ", 1, 2, "Escolha 1 ou 2")
    if eh_campeonato == 2:
        print("\nVocê escolheu um campeonato!\n")
    else:
        print("\nVocê escolheu um jogo!\n")
        partida()


main()
