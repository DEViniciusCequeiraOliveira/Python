def verificar_matrize(matriz):
    for numLinhas, i in enumerate(matriz):
        for numColunas, j in enumerate(i):
            pass

    return numLinhas, numColunas

def soma_matrizes(m1,m2):
    matrizSomada = []

    if verificar_matrize(m1) == verificar_matrize(m2):
        for i1, i2 in zip(m1, m2):
            linhaSomada = []

            for j1, j2 in zip(i1, i2):
                valor = j1 + j2
                linhaSomada.append(valor)
            matrizSomada.append(linhaSomada)
    else:
        return False

    return matrizSomada


print(soma_matrizes([[1]],[[2]]))