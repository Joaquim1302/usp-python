n = 191234536

i = n
while i // 10 != 0:
    j = (i % 100) // 10
    k = i % 10
    if j == k:
        print("a resposta é sim")
        break
    i //= 10
if j != k:
    print("a resposta é não")
