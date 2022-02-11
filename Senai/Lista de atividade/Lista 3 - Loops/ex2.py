# 2. Faça um programa em Python que mostre uma tabela de conversão de graus fahrenheit
# para centígrados para todos valores inteiros de 32 a 80 farenheit, mostrando o valor em
# centígrados e ao lado o valor em fahrenheit. A conversão de graus fahrenheit para
# centígrados é obtida por fahrenheit = (9*centígrados/5)+32.


for farenheit in range(32, 81):
    celsius = 5 * (farenheit - 32) / 9
    print(f"{farenheit} ºF ........ {celsius:.2f} ºC")
