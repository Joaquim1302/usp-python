def soma_lista(lista) -> int:
    """Soma uma lista usando recurção"""
    # Caso base
    if len(lista) == 1:
        return lista[0]
    # Caso recursivo
    return lista[0] + soma_lista(lista[1:])


# if __name__ == "__main__":
#     a = [1, 2, 3, 4, 5, 16]
#     print(soma_lista(a))
