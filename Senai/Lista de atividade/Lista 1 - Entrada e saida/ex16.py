# 16. Um grupo de amigos pretende alugar um carro por um único dia. Consultadas duas
# agências, a primeira cobra R$62,00 pela diária e R$1,40 por quilômetro rodado. A segunda
# cobra diária de R$80,00 e mais R$1,20 por quilômetro rodado. Escreva um programa em
# Python que leia a quantidade de quilômetros a serem rodados e calcule e imprima na tela
# o preço a ser pago em cada uma das agências.

km = float(input("Quantos km foi rodado? "))

agencia1 = 62 + 1.4 * km
agencia2 = 80 + 1.2 * km

print(f"O valor na agência 1 é R$ {agencia1:.2f} e na agência 2 é R$ {agencia2:.2f}")