def baseDecimalParaOutra(n, base):
    lista = []

    n = int(n)
    while n > 0:

        numBase = n % base
        n = n // base

        numBase = str(numBase)

        if numBase == "10":
            numBase = "A"
        elif numBase == "11":
            numBase = "B"
        elif numBase == "12":
            numBase = "C"
        elif numBase == "13":
            numBase = "D"
        elif numBase == "14":
            numBase = "E"
        elif numBase == "15":
            numBase = "F"

        lista.append(numBase)
    lista.reverse()
    resultado = "".join(lista)
    return resultado
