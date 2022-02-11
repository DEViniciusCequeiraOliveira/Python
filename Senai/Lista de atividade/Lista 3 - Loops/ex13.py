# 13. Escreva um programa em Python que leia números inteiros até que a soma de tais
# números totalize no mínimo 100. Devem ser lidos tantos valores quantos necessários para
# que o limite seja atingido ou superado. Quando isto ocorrer, o programa também deve
# exibir quantos números foram lidos e sua média

cont = 0
soma = 0

while soma < 100:
    cont += 1
    numero = int(input(f"Digite o {cont}º número: "))
    soma += numero

print(f"Foram digitados {cont} numeros e a média foi {soma/cont}")