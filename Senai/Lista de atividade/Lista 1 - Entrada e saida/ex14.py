# 14. Faça um programa em Python que leia uma temperatura fornecida em graus fahrenheit
# e a converta para o seu equivalente em graus centígrados, imprimindo este valor na tela.
# Dado:

fahrenheit = float(input("Qual a temperatura em ºF? "))

celsisus = (5/9) * (fahrenheit-32)

print(f"A sua temperatura é {celsisus:.2f} ºC")