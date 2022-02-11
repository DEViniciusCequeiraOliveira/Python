# 4. Faça um programa em Python que leia 10 valores, um de cada vez, e apresente o maior
# deles ao final
numMaximo = 0

for cont in range(0, 10):
    num = float(input("Digite um nùmero: "))

    if num > numMaximo:
        numMaximo = num

print("O maior número é", numMaximo)