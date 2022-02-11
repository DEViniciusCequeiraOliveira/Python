

def e_hipotenusa(numero):
    n1 = 1
    n2 = 1
    somas = []
    numero = numero ** 2
    while numero > n1:
        n1 += 1
        while numero > n2:
            num1 = n1 ** 2
            num2 = n2 ** 2
            soma = num1 + num2

            print(soma)
            if (soma <= numero) and (num1 != num2) and (soma not in somas):
                somas.append(soma)
            n2 += 1
        n2 = 1
    somas.sort()
    print(somas)
    return somas

def soma_hipotenusas(numero):
    soma = 0
    numeros = e_hipotenusa(numero)
    for n in numeros:
        soma += n

    return soma

e_hipotenusa(25)