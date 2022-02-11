# 22. Escreva um programa em Python que calcula um reajuste salarial, de acordo com as
# regras a seguir:
#  Se o salário for menor que R$ 500,00 então o reajuste é de 15%
#  Se o salário estiver entre R$ 500,00 e R$ 1.000,00 então o reajuste é de
# 8%
#  Se o salário for superior R$ 1.000,00 então o reajuste é de 3%

salario = float(input("Digite o seu salário: "))

if salario < 500 and salario > 0:
    salario *= 115/100
    print("O seu salário é R$", salario)

elif salario >= 500 and salario < 1000:
    salario *= 108/100
    print("O seu salário é R$", salario)

elif salario >= 1000:
    salario *= 103/100
    print("O seu salário é R$", salario)

else:
    print("Valor não existe :(")