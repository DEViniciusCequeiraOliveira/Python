# 29. Uma agência de viagens quer disponibilizar a seus passageiros que chegam ao Brasil
# um terminal de conversão de taxa de câmbio. Tal terminal será utilizado num aeroporto
# que recebe principalmente passageiros norte-americanos, europeus e japoneses. Escreva
# um programa em Python que leia do teclado a opção desejada: converter dólares, euros
# ou ienes para reais, leia a quantia em moeda estrangeira e apresente na tela o valor dado
# e seu equivalente em reais.
# Considere:
# 1,00 DÓLAR = R$ 4,12
# 1,00 EURO = R$ 4,59
# 1,00 IENE = R$ 0,038

print("Escolhar uma opção:"
      "\nA) Converter Dólar"
      "\nB) Converter Euro"
      "\nC) Converter Iene")

resposta = input()

if resposta == "A":
    dolar = float(input("Digite quantos dolares você tem: "))
    real = 4.12 * dolar
    print("Voce tem R$", real)

elif resposta == "B":
    euro = float(input("Digite quantos euros você tem: "))
    real = 4.59 * euro
    print("Voce tem R$", real)

elif resposta == "C":
    iene = float(input("Digite quantos iene você tem: "))
    real = 0.038 * iene
    print("Voce tem R$", real)