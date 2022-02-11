# 17. Escreva um programa em Python que calcule o valor do desconto de uma mercadoria
# paga a vista e o valor total a ser pago. O programa deve ler o valor da mercadoria e a
# porcentagem do desconto. Depois o programa deve calcular e imprimir na tela o valor do
# desconto e o novo valor da mercadoria com o desconto.

valorMercadoria = float(input("Qual o valor da mercadoria? "))
porDesconto = float(input("Qual a porcentagem de desconto? "))

desconto = valorMercadoria * (porDesconto/100)

valorNovo = valorMercadoria - desconto

print(f"O desconoto foi de R$ {desconto:.2f} e o valor final vai ser R$ {valorNovo:.2f}")
