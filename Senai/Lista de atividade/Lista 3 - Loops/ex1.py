# 1. Faça um programa em Python que solicite dois números inteiros positivos e exiba os
# múltiplos de 7 existentes entre estes números. Faça uma versão com cada um dos laços:
# for e while.

numInicial = int(input("Digite o número inicial: "))
numFinal = int(input("Digite o número final: "))
contador = 0
num = numInicial

# while num <= numFinal:
#     resto = num % 7
#     if resto == 0:
#         contador += 1
#     num += 1
#
# print(f"Entre {numInicial} e {numFinal} tem {contador} múltiplos de 7")


for cont in range(numInicial, numFinal + 1):
    resto = num % 7
    if resto ==0:
        contador +=1
    num += 1

print(f"Entre {numInicial} e {numFinal} tem {contador} múltiplos de 7")

