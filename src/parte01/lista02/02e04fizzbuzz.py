n = int(input("Digite um nº inteiro: "))
resto3 = n % 3
resto5 = n % 5
if (resto3 == 0 and resto5 == 0):
    print("FizzBuzz")
else:
    print(n)
