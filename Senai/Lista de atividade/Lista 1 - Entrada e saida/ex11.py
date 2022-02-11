# 11. Escreva um programa em Python que leia os valores da base maior (B), base menor
# (b) e altura (h) de um trapézio e calcule e imprima o valor de sua área, sabendo que a área
# de um trapézio (A) é dada por

baseMaior = float(input("Qual a base maior do trapézio em cm? "))
baseMenor = float(input("Qual a base menor do trapézio em cm? "))
altura = float(input("Qual a altura do trapézio em cm? "))

area = ((baseMaior + baseMenor) * altura) / 2

print(f"Sua área é {area:.2f} cm²")