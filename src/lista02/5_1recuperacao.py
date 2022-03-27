notaArr = [6,   2.3,   3,   5.0,  6.5,  8.7,  4.9]
recup = 0
for nota in notaArr:
    if nota >= 3 and nota < 5:
        recup += 1
print("Numero de alunos de recuperacao =", str(recup))
