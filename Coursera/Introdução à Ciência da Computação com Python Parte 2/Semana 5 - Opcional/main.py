def  insertion_sort(lista):
    for i in range(len(lista)):
        elemento = lista[i]

        while i > 0 and lista[i - 1] > elemento:
            lista[i] = lista[i - 1]
            i -= 1

        lista[i] = elemento

    return lista