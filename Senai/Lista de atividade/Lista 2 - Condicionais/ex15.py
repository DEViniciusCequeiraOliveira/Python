# 15. Escreva um programa em Python que verifique se um ano lido é ano de copa do
# mundo. Seu programa deve permitir a leitura do ano, depois realizar os testes necessários
# e exibir na tela a mensagem de que é ou não ano de copa do mundo. Considerando que
# um ano de copa do mundo é divisível por 2 e não é divisível por 4.

ano = int(input("Digite o ano: "))

div2 = ano % 2
div4 = ano % 4

if div2 == 0 and not div4 == 0:
    print("Ano de Copa do Mundo !!!")

else:
    print("Não vai ter copa :(")