# 9. Escreva um programa em Python que leia n números inteiros positivos fornecidos e
# imprima na tela uma mensagem informando se o número é ou não perfeito.
# Obs.: Número perfeito é aquele cuja soma de seus divisores, exceto ele próprio, é igual ao
# número.
# Ex.: 6 = 1 + 2 + 3

n = int(input("Digite um número: "))
soma = 0

for i in range(1,n):
    if n % i == 0:
        soma += i


if soma == n:
    print("Número perfeito")

else:
    print("Número não perfeito")
