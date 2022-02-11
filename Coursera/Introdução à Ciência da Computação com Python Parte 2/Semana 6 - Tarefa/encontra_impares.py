impar = []

def eImpar(numero):
    if not numero % 2 == 0:
        return True
    else:
        return False

def encontra_impares(lista, i=0, max = None):
    if max == None:
        max = len(lista) -1

    if max == -1:
        return impar

    else:
        if eImpar(lista[i]):
            impar.append(lista[i])
            i += 1
            return encontra_impares(lista[i:])
        else :
            i += 1
            return encontra_impares(lista[i:])
