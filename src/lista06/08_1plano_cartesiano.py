x_pos = x = float(input("Digite x: "))
y = float(input("Digite y: "))

if x < 0:
    x_pos = -x

# face == True se (x,y) esta na face
face = x_pos < 5 and 0 < y < 8

# boca == True se (x,y) esta na boca
boca = x_pos <= 3 and 1 <= y <= 2

# olho == True se (x,y) esta em um dos olhos
olho = 1 <= x_pos <= 4 and 4 <= y <= 7

# iris == True se (x,y) esta em uma das iris
iris = 2 < x_pos < 3 and 5 < y < 6

# vixe! :-D complicado?! certamente muito elegante
if iris or face and not (boca or olho):
    print("dentro")
else:
    print("fora")
