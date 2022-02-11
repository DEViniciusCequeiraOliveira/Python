# 23. Uma empresa possui um esquema de pontuação que determina o valor de um bônus.
# Essa pontuação é dada através da seguinte fórmula:
# Pontos = Horas extras – 2/3 * Faltas
# Escreva um algoritmo/programa em Python que leia de um empregado, as horas extras
# trabalhadas e as horas de faltas e determine o bônus que é dado pela seguinte tabela:
# Pontos Bônus
# > 40 R$ 5.000,00
# Maior que 30 e menor ou igual a 40 R$ 4.000,00
# Maior que 20 e menor ou igual a 30 R$ 3.000,00
# Maior que 10 e menor ou igual a 20 R$ 2.000,00
# ≤ 10 R$ 1.000,0

horaExtra = int(input("Digite a quantidade de horas extras trabalhadas: "))
horaFalta = int(input("Digite a quantidade de horas faltas: "))

pontos = horaExtra - 2/3 * horaFalta

if pontos > 0 and pontos <= 10:
    print(f"Você ganhou R$ 1.000,00 de bônus, você teve {pontos} pontos")

elif pontos > 10 and pontos <= 20:
    print(f"Você ganhou R$ 2.000,00 de bônus, você teve {pontos} pontos")

elif pontos > 20 and pontos <= 30:
    print(f"Você ganhou R$ 3.000,00 de bônus, você teve {pontos} pontos")

elif pontos > 30 and pontos <= 40:
    print(f"Você ganhou R$ 4.000,00 de bônus, você teve {pontos} pontos")

elif pontos > 40:
    print(f"Você ganhou R$ 5.000,00 de bônus, você teve {pontos} pontos")

else:
    print(f"Sem bônus :(")