def first_lexi(texto):
    fst = texto[0]
    for wrd in texto:
        if wrd < fst:
            fst = wrd
    return fst


text = [
    "ana",
    "maria",
    "José",
    "Valdemar"
]

print(first_lexi(text))
