# 27. Escreva um programa em Python que leia do teclado dois valores quaisquer, guardeos em duas variáveis ‘a’ e ‘b’ e, a seguir, troque os valores associados a estas duas
# variáveis. O valor original armazenado em ‘b’ deve passar para ‘a’ e o valor original de ‘a’
# deve passar para b.
# Obs.: note que a sequência de comandos a=b; b=a; não vai funcionar! Por quê?

a = input("Digite o valor A: ")
b = input("Digite o valor B: ")

temp = a
a = b
b = temp

print(f"O valor de A é: {a} e o de B é: {b}")