def maximo(x, y, z):
    mx = x
    if mx < y:
        mx = y
    if mx < z:
        mx = z
    return mx


x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

print(maximo(x, y, z))
