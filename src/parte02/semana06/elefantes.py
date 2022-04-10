def incomodam(n):
    if n < 1:
        return ''
    return 'incomodam ' + incomodam(n - 1)


def elefantes(n):
    if n < 2:
        return ''
    elif n == 2:
        return 'Um elefante incomoda muita gente\n' + str(n) + \
            ' elefantes ' + incomodam(n) + 'muito mais\n'
    return elefantes(n - 1) + str(n - 1) + \
        ' elefantes incomodam muita gente\n' + \
        str(n) + ' elefantes ' + incomodam(n) + 'muito mais\n'


# if __name__ == "__main__":
#     print(elefantes(1))
