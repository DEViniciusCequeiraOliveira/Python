# 28. Infrações de trânsito e acidentes em geral estão muitas vezes relacionados com
# excesso de velocidade. Pensando nisso a secretaria do DETRAN reajustou o valor das
# multas e encomendou a você um programa que calcule os novos valores, válidos para as
# rodovias federais. Se a velocidade do veículo for até a velocidade permitida, o condutor
# não paga multa; caso ela exceda em até 20% a velocidade permitida, o valor da multa é de
# R$ 250; e caso o excesso seja superior à 20% a multa é de R$750. Escreva um programa
# em Python que leia do teclado a velocidade máxima permitida e a velocidade na qual o
# veículo trafegava, apresentando na tela o valor da multa a ser pago.

velocidadeTrafegada = float(input("Digite a velocidade trafegada pelo carro em Km/h: "))
velocidadeMaxima = float(input("Digite a velocidade máxima em Km/h: "))
velocidade20Por = velocidadeMaxima * 120/100

if velocidadeTrafegada <= velocidadeMaxima:
    print("Não paga multa!!!")

elif velocidadeTrafegada > velocidadeMaxima:
    if velocidadeTrafegada <= velocidade20Por:
        print("Multa de R$ 250,00")

    elif velocidadeTrafegada > velocidade20Por:
        print("Multa de R$ 750,00")