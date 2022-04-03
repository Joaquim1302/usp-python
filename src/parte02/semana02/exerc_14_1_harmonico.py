def harmonico(n):
    soma_harm = 0.0
    for i in range(1, n + 1):
        soma_harm += 1 / i
    return soma_harm


if __name__ == "__main__":
    for j in range(10):
        print("harmonico " + str(j) + ": ", harmonico(j))
