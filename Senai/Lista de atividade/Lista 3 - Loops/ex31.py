# 31. Faça um programa em Python que leia uma quantidade não determinada de números
# positivos. Calcule a média dos valores pares, a média de valores ímpares e a média geral
# dos números lidos. A leitura encerrará quando for digitado um valor menor ou igual a zero.

def media(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma / len(lista)

pares = []
impares = []

n = int(input("Digite um número: "))

while n > 0:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    n = int(input("Digite um número: "))

print(f"A média de valores pares é {(media(pares)):.2f} e a média impares {media(impares):.2f}")
print(f"A média Geral foi: {media(pares + impares):.2f}")