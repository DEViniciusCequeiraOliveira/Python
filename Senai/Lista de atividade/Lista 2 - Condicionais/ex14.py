# 14. A prefeitura de uma cidade abriu uma linha de crédito para os funcionários estatutários.
# O valor máximo da prestação não poderá ultrapassar 30% do salário bruto. Faça um
# programa em Python que permita entrar com o salário bruto e o valor da prestação, e
# informar se o empréstimo pode ou não ser concedido.

salario = float(input("Digite o seu salário: "))
prestacao = float(input("Digite o valor da prestação: "))

maxprestacao = salario * 130/100

if prestacao <= maxprestacao:
    print("Pode ocorrer o emprestimo. Partiu Dubai !!!")

else:
    print("O emprestimo não pode ocorrer :(")
