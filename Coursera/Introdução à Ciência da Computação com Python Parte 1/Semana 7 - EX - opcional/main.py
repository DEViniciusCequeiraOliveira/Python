def ePrimo(numero):
    for num in range(2,numero):
        if numero % num == 0:
            return False

    return True

def n_primos(n):
    cont = 0
    while n >= 2:
        primo = ePrimo(n)
        if primo:
            cont += 1
        n-= 1
    return cont

