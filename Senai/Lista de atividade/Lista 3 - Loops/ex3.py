# 2. Faça um programa em Python que mostre uma tabela de conversão de graus fahrenheit
# para centígrados para todos valores inteiros de 32 a 80 farenheit, mostrando o valor em
# centígrados e ao lado o valor em fahrenheit. A conversão de graus fahrenheit para
# centígrados é obtida por fahrenheit = (9*centígrados/5)+32.

# 3. Altere o programa anterior para que o usuário informe qual o valor inicial e o valor final
# em farenheit e informe também o intervalo entre estes valores para conversão (de um em
# um, de dois em dois, etc.).

tempInicial = int(input("Digite a temperatura inicial em Farenheit: "))
tempFinal = int(input("Digite a temperatura final em Farenheit: "))
intervaloTemp = int(input("Digite o intervalo das temperaturas: "))

for farenheit in range(tempInicial, tempFinal+1, intervaloTemp):
    celsius = 5 * (farenheit - 32) / 9
    print(f"{farenheit}ºF ........ {celsius:.2f}ºC ")