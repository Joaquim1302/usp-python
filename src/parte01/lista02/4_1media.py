notaArr = [6,   2.3,   3,   5.0,  6.5,  8.7,  4.9]
med = float(0)
n = 0
for nota in notaArr:
    med += nota
    n += 1
med /= n
print("Média:", str(med))
