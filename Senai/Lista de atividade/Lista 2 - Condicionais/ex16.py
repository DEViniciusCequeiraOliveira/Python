# 16. Faça um programa em Python que lê a altura em metros e o sexo de uma pessoa
# (masculino ou feminino), e calcula e mostra o peso ideal, utilizando as seguintes fórmulas:
#  Para homens: (72.7 * altura) - 58
#  Para mulheres: (62.1 * altura) - 44.7

altura = float(input("Digite a sua altura em m: "))
sexo = input("Masculino ou Feminino M/F: ")

if sexo == "M":
    peso = (72.7 * altura) - 58
    print(f"O seu peso ideal é {peso:.2f} Kg")

elif sexo == "F":
    peso = (62.1 * altura) - 44.7
    print(f"O seu peso ideal é {peso:.2f} Kg")