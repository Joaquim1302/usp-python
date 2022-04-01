def ehLetra(c):
    ac = ord(c)
    return (ac >= 65 and ac <= 90) or (ac >= 97 and ac <= 122)


def vogal(c):
    vogais = ["a", "e", "i", "o", "u"]
    letra = c.lower()
    return letra in vogais


st = input("Digite um único caractere: ")
if len(st) > 1:
    print("Foram digitados mais de 1 caracter")
elif ehLetra(st):
    print(vogal(st))
else:
    print("Esse digito não é uma letra")
