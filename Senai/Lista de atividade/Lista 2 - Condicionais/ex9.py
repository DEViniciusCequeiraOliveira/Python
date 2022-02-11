# 9. Para ser apta a doar sangue a pessoa deve ter entre 18 e 65 anos e pesar no mínimo
# 50kg. Escreva um programa em Python que leia a idade e o peso de uma pessoa e
# apresente na tela uma mensagem informando se ela pode ser doadora ou não.

idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o peso em Kg: "))

if 18 <= idade and 65 >= idade and 50 < peso:
    print("Você pode doar sangue!!!")

else:
    print("Você não pode doar sangue :(")