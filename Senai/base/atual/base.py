def decimal(num, base): #Essa função faz a conta das sucessivas multiplicações (ela pega o digito multiplica pela base elevada a posição)
                        #digito X base ^ posição + .....
    num = str(num)

    base = int(base)

    decimalTotal = 0

    lista = []

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
    
    potencia = len(num)-1

    for a in (lista):
        decimalN = a * (base) ** (potencia)
        potencia -=1
        decimalTotal += decimalN

    return decimalTotal


def outra(n, base): #Essa função faz a conta das sucessivas divisões (ela pega o numero e divide pele base destino e depois junta os restos de tras para frente)
                    #ela pega o numero e divide pele base destino e depois junta os restos de tras para frente
    lista = []

    n = int(n)
    while n > 0:

        nume_ba = n % base
        n = n // base

        nume_ba = str(nume_ba)

        if nume_ba == "10":
            nume_ba = "A"
        elif nume_ba == "11":
            nume_ba = "B"
        elif nume_ba == "12":
            nume_ba = "C"
        elif nume_ba == "13":
            nume_ba = "D"
        elif nume_ba == "14":
            nume_ba = "E"
        elif nume_ba == "15":
            nume_ba = "F"

        lista.append(nume_ba)

    lista.reverse()
    resultado = "".join(lista)

    return resultado
