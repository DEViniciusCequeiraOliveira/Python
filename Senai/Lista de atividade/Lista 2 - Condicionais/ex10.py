# 10. Uma determinada companhia aérea só contrata aeromoças que preencham os
# seguintes requisitos:
# - Ter idade igual ou superior a 24 anos.
# - Ter altura igual ou superior a 1.70 m.
# - Falar com fluência 2 ou mais idiomas.
# Escreva um programa em Python que leia a idade, a altura e a quantidade de idiomas
# falados com fluência de uma candidata e imprima uma mensagem informando se essa
# candidata atende ou não aos requisitos da companhia aérea.

idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura em m: "))
idiomas = int(input("Digite a quantidade de idiomas que fala com fluência: "))

if idade >= 24 and altura >= 1.7 and idiomas >=2:
    print("Parabéns você conquistou a vaga!!!")

else:
    print("Você não atendeu todos os requisitos :(")