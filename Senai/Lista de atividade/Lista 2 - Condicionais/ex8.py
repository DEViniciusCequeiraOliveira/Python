# 8. Faça um programa em Python que peça para o usuário pensar em número de 1 a 4 e
# depois pergunte se o número é maior que 2 (S-Sim ou N-Não), e caso seja maior que 2,
# pergunte se ele é maior que 3, ou caso não seja maior que 2, pergunte se é maior que 1.
# Ao final o programa deve mostrar o número que o usuário pensou.

print("Pense em um número de 1 a 4\n")

afimacao1 = input("O número que você pensou é MAIOR que 2? S/N ")

if afimacao1 == "S":
    afimacao2 = input("O número que você pensou é MAIOR que 3? S/N ")

    if afimacao2 == "S":
        print("Seu número é 4")
    elif afimacao2 == "N":
        print("Seu número é 3")

elif afimacao1 == "N":
    afimacao2 = input("O número que você pensou é MAIOR que 1? S/N ")

    if afimacao2 == "S":
        print("Seu número é 2")
    elif afimacao2 == "N":
        print("Seu número é 1")