def ePrimo(k):
    valor = 1
    count = 0

    while valor <= k or count > 2:
        resto = k % valor
        valor += 1
        if resto == 0:
            count += 1

    if count > 2:
        return False

    else:
        return True


def maior_primo(numero):
    n = numero
    ePrimo(n)
    while n > 1 and ePrimo(n) == False:
        ePrimo(n)
        n -= 1

    return n