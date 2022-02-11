# 12. Escreva um programa em Python que leia o peso e a altura de uma pessoa. Em
# seguida o programa deve calcular e imprimir índice de massa corpórea (IMC) dessa
# pessoa. Dado:

from math import pow

peso = float(input("Qual o peso em Kg? "))
altura = float(input("Qual a sua altura? "))

imc = (peso) / (pow(altura, 2))

print(f"O seu IMC é {imc:.2f} Kg/m²")