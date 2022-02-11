def remove_repetidos(lista):
    list=[]
    for n in lista:
        if not n in list:
            list.append(n)
    list.sort()
    return list