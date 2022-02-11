# 12. Uma empresa quer dar uma bonificação para determinados funcionários. Deverão
# receber um bônus de R$ 500,00 no salário os funcionários com mais de 50 anos ou que
# trabalhem na empresa há pelo menos 5 anos. Escreva um programa em Python que leia a
# idade, o tempo de serviço (em anos) e o salário do funcionário e imprima na tela o valor do
# salário a ser recebido.

idade = int(input("Digite a sua idade: "))
tempEmpresa = int(input("Digite o seu tempo na empresa: "))
salario = float(input("Digite o seu salário R$ "))

if idade > 50 or tempEmpresa >= 5:
    salario += 500
    print(f"Você vai receber R$ {salario:.2f}")

else:
    print(f"Você não vai receber o bônus, então vai ficar com R$ {salario:.2f}")

