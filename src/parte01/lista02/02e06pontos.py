from math import sqrt


x1 = int(input("P1 x: "))
y1 = int(input("P1 y: "))
x2 = int(input("P2 x: "))
y2 = int(input("P2 y: "))

d = sqrt((x1 - x2)**2 + (y1-y2)**2)
if(d >= 10):
    print("longe")
else:
    print("perto")
