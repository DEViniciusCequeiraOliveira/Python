# 13. Escreva um programa em Python para calcular o salário semanal de uma pessoa,
# determinado pelas seguintes condições. Se o número de horas trabalhadas for menor ou
# igual a 40, a pessoa recebe 8 reais por hora trabalhada, se não a pessoa recebe 320 reais
# fixos e mais 12 reais para cada hora trabalhada que excede 40 horas. (Exemplo: uma
# pessoa que trabalha 42 horas deve receber 344 reais). Seu programa deve ler o número
# de horas trabalhadas e deve imprimir na tela o salário semanal.

tempTrabalhado = int(input("Digite o tempo trabalhado em horas: "))

if tempTrabalhado <= 40 and tempTrabalhado > 0:
    salario = tempTrabalhado * 8
    print("O seu salário é R$", salario)

elif tempTrabalhado > 40:
    salario = 320 + ((tempTrabalhado - 40) * 12)
    print("O seu salário é R$", salario)
