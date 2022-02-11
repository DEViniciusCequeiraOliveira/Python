# 17. Um americano em visita ao Brasil tinha muita dificuldade na hora de escolher entre
# “bermudas” ou “calças”, pois ele não entendia nossa medida de temperatura (celsius).
# Escreva um programa em Python que, após a entrada da temperatura em Celsius (C),
# escreva a temperatura em Fahrenheits (F) e também o que vestir. Dado que:
# F = (9C + 160)/5;
# Ele irá vestir:
# calças se F < 65,
# bermudas em caso contrário.

tempCelsius = float(input("Digite a temperatura em ºC "))

tempFahrenheit = (9 * tempCelsius + 160)/5

if tempFahrenheit < 65:
    print(f"Vai de calça, a temperatura é {tempFahrenheit} ºF")

else:
    print(f"Vai de bermuda, a temperatura é {tempFahrenheit} ºF")