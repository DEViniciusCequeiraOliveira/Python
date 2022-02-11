def ordenada(lista):
    cont = 0
    fim = len(lista)
    for i in range(fim - 1):
        posicao_do_minimo = i

        for j in range(i+1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                return False

    return True