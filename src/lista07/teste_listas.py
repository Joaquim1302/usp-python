print()
#        0   1  2  3   4   5   6   7   8   9  10  11  12  13  14
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
          67, 71, 73, 79, 83, 89, 97]
for x in range(5, 10):
    print(primos[x])

print(primos[2:7])
print(primos[7:25])
print(primos[2:7])
final = primos[7:]
print(final)
final_2 = final  # aponta para a mesma lista
final_2 = final[:]  # copia para uma nova lista
final_2[len(final_2) - 1] = 100
print(final)
print(final_2)
print(primos)

cores = ["azul", "violeta", "azul", "amarelo", "verde"]
print(cores)
# pertinência
if "amarelo2" in cores:
    print(cores[3], "está")
else:
    print("não está")
# concatenação
nova_lista = primos[2:7] + primos[7:25]
print(primos)
# repetição
a = (primos[2:7] + [0] * 3) * 3
print(a)
# remoção de elementos em listas
del a[1]
del a[1:5]
print(a)
# contagem de elementos
print("0:", a.count(0))

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(alfabeto[0:13])
print(len(alfabeto))
letras = alfabeto[1:10]
print(letras, len(letras))

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes_2 = carnes
print(carnes[-1])
del carnes_2[-1]

print(carnes)
print(carnes_2)
