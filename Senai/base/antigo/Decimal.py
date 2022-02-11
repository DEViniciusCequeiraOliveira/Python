def baseOutraParaDecimal(num, base):
    decimal = 0
    lista = []
    num = str(num)

    for n in num:
        if n == "A":
            n = 10
        elif n == "B":
            n = 11
        elif n == "C":
            n = 12
        elif n == "D":
            n = 13
        elif n == "E":
            n = 14
        elif n == "F":
            n = 15

        n = int(n)
        lista.append(n)

    cont = len(num) - 1

    for a in (lista):
        deci = a * (base) ** (cont)
        cont -= 1
        decimal += deci
    return decimal