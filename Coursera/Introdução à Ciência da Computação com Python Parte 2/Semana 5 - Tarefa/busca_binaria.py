def localiza(lista, elemento):
    for i, n in enumerate(lista):
        if n == elemento:
            return i


def  busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        print(localiza(lista, lista[meio]))
        if lista[meio] == elemento:
            return localiza(lista, lista[meio])

        else:
            if elemento < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1

    return False