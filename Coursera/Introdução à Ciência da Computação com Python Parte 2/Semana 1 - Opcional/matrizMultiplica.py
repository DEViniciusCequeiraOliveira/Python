def tam_matriz(matriz):
    for numLinha, i in enumerate(matriz):
        for numColuna, j in enumerate(i):
            pass

    return [numLinha, numColuna]


def sao_multiplicaveis(m1, m2):
    [numLinhaM1, numColunaM1] = tam_matriz(m1)
    [numLinhaM2, numColunaM2] = tam_matriz(m2)

    if numColunaM1 == numLinhaM2:
        return True

    return False
