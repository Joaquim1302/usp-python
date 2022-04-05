

def main():
    semente = int(
        input("Digite a semente para gerar numeros pseudo-aleatorios: "))
    jogo = Simulador(semente)

    fim = False
    while not fim:
        jogo.sorteia()
        opcao = input("Deseja utilizar o volume sorteado? (s/n): ")
        if opcao == 's':
            fim = jogo.deposita()  # retorna True caso o balde fique cheio
        else:
            fim = True
    jogo.finaliza()


class Simulador:
    def __init__(self, semente):
        print("construtor do Simulador")

    def sorteia(self):
        print("metodo sorteia do Simulador")

    def deposita(self):
        print("metodo deposita do Simulador")

    def finaliza(self):
        print("metodo finaliza do Simulador")    


class Balde:
    def __init__(self):
        print("metodo construtor de Balde")


main()
