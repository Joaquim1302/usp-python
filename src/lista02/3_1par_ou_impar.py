arr = [6,   -2,   7,   0,  -5,   8,  4]
nPar = 0
nImpar = 0
for n in arr:
    if n % 2 == 0:
        nPar += 1
    else:
        nImpar += 1
print(str(nPar), "pares", str(nImpar), "ímpares")
