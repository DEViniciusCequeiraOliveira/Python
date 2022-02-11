lista = [4,0,7,1,24,7,5,6,4,5,5,4,8,7,8]

for i in range(len(lista)):
    elemento = lista[i]

    while i > 0 and lista[i - 1] > elemento:
        lista[i] = lista[i - 1]
        i -= 1

    lista[i] = elemento


print(lista)