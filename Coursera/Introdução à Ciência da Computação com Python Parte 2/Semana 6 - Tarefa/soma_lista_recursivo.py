def soma_lista(lista):
    tamanho = len(lista)
    if tamanho <= 0:
        return 0
    else:
        return lista[tamanho-1] + (soma_lista(lista[:tamanho-1]))
