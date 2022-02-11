# 18. Escreva um programa em Python para ajudar a calcular a quantidade de gotas de um
# remédio que uma determinada criança precisa tomar. A bula desse remédio pediátrico
# recomenda a seguinte dosagem: 5 gotas para cada 2 kg do peso da criança. Você deve
# fazer um programa que leia o peso desta criança, calcule e imprima na tela a quantidade
# de gotas a ser tomada.

peso = float(input("Qual o peso da criança em Kg? "))

gotas = (5 * peso) // 2

print(f"A criança precisa de {gotas} gotas")