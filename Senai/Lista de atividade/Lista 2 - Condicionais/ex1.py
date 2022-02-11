# 1. Um ângulo é chamado agudo se é menor que 90 graus, obtuso se é maior do que 90
# graus ou reto caso seja exatamente 90 graus. Implemente um programa em Python que
# receba um ângulo (número real) como entrada e responda qual é o tipo de ângulo.

angulo = int(input("Qual o valor do ângulo? "))

if angulo < 90:
    print("É agudo")

elif angulo > 90:
    print("É obtuso")

elif angulo == 90:
    print("é reto")

else:
    print("Não tem como?!")
