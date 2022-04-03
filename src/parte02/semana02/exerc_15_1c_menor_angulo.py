import exerc_15_1b_angulo as exer15_1


def main():
    pontos = [[2, 5], [5, 4], [9, 1], [4, 4], [1, 3]]
    menor_ang = exer15_1.angulo_graus(pontos[0][0], pontos[0][1])
    n_pontos = len(pontos)
    for i in range(n_pontos):
        ang = exer15_1.angulo_graus(pontos[i][0], pontos[i][1])
        if ang < menor_ang:
            menor_ang = ang
        print(f"[{pontos[i][0]:2g},{pontos[i][1]:2g}]:",
              f"{ang: 5.2f}º")
    print("Menor ângulo:", f"{menor_ang: 5.2f}º")


if __name__ == "__main__":
    main()
