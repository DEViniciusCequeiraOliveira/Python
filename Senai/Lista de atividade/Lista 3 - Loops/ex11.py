# 11. Escreva um programa em Python que imprime a soma de todos os números inteiros
# entre A e B (incluindo A e B), onde A e B são fornecidos pelo usuário.

numInicial = int(input("Digite um número inicial: "))
numFinal = int(input("Digite um número final: "))
soma = 0

for num in range(numInicial, numFinal + 1):
    soma += num

print(soma)