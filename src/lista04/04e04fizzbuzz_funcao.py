def fizzbuzz(n):
    fizz = (n % 3) == 0
    buzz = (n % 5) == 0
    if fizz and buzz:
        print("FizzBuzz")
    elif fizz:
        print("Fizz")
    elif buzz:
        print("Buzz")
    else:
        print(n)


n = int(input("Digite um nº inteiro: "))
fizzbuzz(n)
