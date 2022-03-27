notaArr = [6,   2.3,   3,   5.0,  6.5,  8.7,  4.9]
med = 0.0
n = 0
reprv = 0
recup = 0
aprov = 0
topGun = 0
for nota in notaArr:
    if nota < 3:
        reprv += 1
    elif nota >= 3 and nota < 5:
        recup += 1
    elif nota >= 5:
        aprov += 1
    if nota > 8:
        topGun += 1
    med += nota
    n += 1
med /= n
print("Média =", str(med))
print("Total de alunos =", str(n))
print("Numero de alunos reprovados =", str(reprv))
print("Numero de alunos de recuperacao =", str(recup))
print("Numero de alunos aprovados =", str(aprov))
print("Numero de alunos com desempenho muito bom =", str(topGun))
