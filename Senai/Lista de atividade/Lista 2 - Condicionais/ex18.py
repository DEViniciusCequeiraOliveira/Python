# 18. Em uma competição esportiva o desempenho de uma equipe é medida pela
# quantidade de medalhas de ouro que a equipe conquista. Escreva um algoritmo/programa
# em Python que leia a quantidade de medalhas de ouro ganhas pela equipe e escreva na
# tela uma mensagem informando o desempenho da equipe de acordo com a tabela abaixo:
#
# maior ou igual a 30 Ótimo
# maior ou igual a 20 e menor que 29 Muito bom
# maior ou igual a 10 e menor que 19 Regular
# menor que 10 Ruim

ouro = int(input("Digite a quantidade de medalhas de ouro que a equipe conquistou: "))

if ouro >= 30:
    print("Ótimo")

elif ouro >= 20 and ouro < 29:
    print("Muito bom")

elif ouro >= 10 and ouro < 19:
    print("Regular")

elif ouro > 0 and ouro < 10:
    print("Ruim")