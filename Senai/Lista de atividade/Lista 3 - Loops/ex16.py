# 16. Escreva um programa em Python que leia o salário de uma pessoa, a quantidade de
# contas (despesas) que uma pessoa precisa pagar em um mês e, para cada conta, leia o
# valor a ser pago. O programa deve somar todos os valores de contas que a pessoa
# necessita pagar e depois verificar se a diferença entre o salário da pessoa e o valor de
# todas as despesas que deve pagar no mês é positiva. Se a diferença (salário – despesas)
# for positiva imprimir este valor da diferença na tela. Se a diferença for negativa imprimir a
# mensagem “reduzir despesas”.

salario = float(input("Digite o seu salário: R$ "))
qntDespesas = int(input("Digite a quantidade de despesas: "))
somaDespesas = 0

while qntDespesas > 0:
    valorDespesas = float(input(f"Digite o valor da despesa {qntDespesas}: R$ "))
    somaDespesas += valorDespesas
    qntDespesas -= 1

if salario >= somaDespesas:
    print(f"\nA diferencia é R$ {salario - somaDespesas}")

else:
    print("\nReduzir despesas")
