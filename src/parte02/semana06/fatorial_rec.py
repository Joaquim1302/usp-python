def fat_rec(n):
    if n <= 1:
        return 1
    return n * fat_rec(n - 1)


if __name__ == "__main__":
    print(fat_rec(5))
