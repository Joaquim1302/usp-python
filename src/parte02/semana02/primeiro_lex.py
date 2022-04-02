def primeiro_lex(lista):
    fst = lista[0]
    for wrd in lista:
        if wrd < fst:
            fst = wrd
    return fst


text = [
    "ana",
    "maria",
    "José",
    "Valdemar"
]

# print(primeiro_lex(text))
# print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))
# print(primeiro_lex(['AAAAAA', 'b']))
