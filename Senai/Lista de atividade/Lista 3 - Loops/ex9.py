# 9. Faça um programa em Python que leia 10 valores, um de cada vez, e conte quantos são
# positivos, mostrando o resultado da contagem ao final.

cont = 0

for c in range(0,10):
    num = int(input("Digite um número: "))
    if num > 0:
        cont += 1

print(f"Você tem {cont} números positivos")