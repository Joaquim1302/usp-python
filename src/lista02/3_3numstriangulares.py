# n = int(input("Encontar os nºs triangulares de 0 a:"))
n = 1000
j = 1
while j <= n:
    i = 1
    while i < j:
        t = i*(i+1)*(i+2)
        if t == j:
            print(str(j), 'é triangular (', str(i),
                  "x", str(i+1), "x", str(i+2), ")")
        i += 1
    j += 1
