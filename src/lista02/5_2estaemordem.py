# nArr = [7,   -6,   0,   12,   15,   37,   101,   201]
nArr = [-6,	  0,   7,	12,	  15,	37,	  101,	 201]
i = 0
l = len(nArr) - 1
while i < l:
    if nArr[i] > nArr[i+1]:
        print("Não está em ordem crescente.")
        break
    i += 1
if i == l:
    print("Está em ordem crescente.")
