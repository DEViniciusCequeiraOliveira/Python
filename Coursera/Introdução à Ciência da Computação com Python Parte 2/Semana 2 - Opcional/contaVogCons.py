asciiInicial = 96
asciiFinal = 123

def conta_letras(frase, contar="vogais"):
    cont = 0
    tuplaVogais = ("a","e","i","o","u")
    for letra in frase:
        letra = letra.lower()
        if contar == "vogais":
            if letra in tuplaVogais:
                cont += 1

        elif contar == "consoantes":
            if letra not in tuplaVogais and ord(letra) >= asciiInicial and ord(letra) <= asciiFinal:
                cont += 1

    return cont

print(conta_letras('programamos em python', 'vogais'))