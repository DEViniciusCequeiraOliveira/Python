from BaseQualquer import baseDecimalParaOutra
from Decimal import baseOutraParaDecimal

numero = str(input("Digite o Numero a ser convertido :")).upper()
base = int(input("""Qual a base
[ 1 ]- Hexadecimal
[ 2 ]- Octadecimal
[ 3 ]- Binária
[ 4 ]- Decimal :"""))

baseFutura = int(input("""Escolha a base para convesão:
[ 1 ]- Hexadecimal
[ 2 ]- Octadecimal
[ 3 ]- Binária
[ 4 ]- Decimal :"""))

if base == 1:
    if baseFutura == 1:
        print(numero)

    elif baseFutura == 2:
        bas = 8
        res = baseOutraParaDecimal(numero, 16)
        res1 = baseDecimalParaOutra(res, 8)
        print(res1)