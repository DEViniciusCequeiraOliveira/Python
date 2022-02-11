def maiusculas(frase):
    nomeFinal = ""
    for letra in frase:
        if ord(letra) >= 65 and ord(letra) <= 90:
            nomeFinal += letra
    return nomeFinal


def test_maiusculas1():
    assert maiusculas('Programamos em python 2?') == "P"

def test_maiusculas2():
    assert maiusculas('Programamos em Python 3.') == "PP"

def test_maiusculas3():
    assert maiusculas('PrOgRaMaMoS em python!') == "PORMMS"