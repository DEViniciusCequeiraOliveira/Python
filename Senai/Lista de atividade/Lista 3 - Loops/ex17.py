# 17. Escreva um programa em Python que leia dois números inteiros e faça a multiplicação
# de um número pelo outro sem utilizar o operador de multiplicação (*). Imprimir na tela o
# valor encontrado.
# Obs: Lembrar que uma multiplicação pode ser definida por uma sucessão de somas.

n1 = int(input("Digite o numero 1 "))
n2 = int(input("Digite o numero 2 "))

soma = 0
for c in range(0,n2):
    soma += n1

print(soma)