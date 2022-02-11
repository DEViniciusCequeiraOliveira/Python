def bubble_sort(lista):
    if len(lista) == 1:
        return lista

    fim = len(lista)
    for i in range(fim-1, 0, -1):
        trocou = False
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
                print(lista)


        if not trocou:
            return lista

    return lista

def busca_binaria(lista, elemento, min=0, max=None):
    contMeio = 0
    if max == None:
        max = len(lista)-1

    if max < min:
        return False
    else:
        meio = min + (max-min)//2
        print(lista[meio])

    if lista[meio] > elemento:
        contMeio += 1
        return busca_binaria(lista, elemento, min, meio - 1)
    elif lista[meio] < elemento:
        contMeio +=1
        return busca_binaria(lista, elemento, meio + 1, max)
    else:
        print(contMeio)
        return meio

a = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]

busca_binaria(a, 99)