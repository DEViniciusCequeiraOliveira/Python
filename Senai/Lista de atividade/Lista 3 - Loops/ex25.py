# 25. Faça um programa em Python que leia uma quantidade não determinada de números
# inteiros. Calcule a quantidade de números positivos e negativos. O número que encerrará
# a leitura será zero.

contPos = 0
contNeg = 0

n = int(input("Digite um número: "))

while n !=0:
    n = int(input("Digite um número: "))

    if n > 0:
        contPos +=1

    elif n < 0:
        contNeg +=1

print(f"Teve {contPos} números positivos e {contNeg} números negativos")