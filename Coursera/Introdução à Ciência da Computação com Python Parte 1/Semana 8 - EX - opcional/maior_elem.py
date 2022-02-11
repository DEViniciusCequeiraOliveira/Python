def maior_elemento(lista):
    for i, n in enumerate(lista):
        if i == 0:
            maiorAtual = n

        elif n > maiorAtual:
            maiorAtual = n

    return maiorAtual