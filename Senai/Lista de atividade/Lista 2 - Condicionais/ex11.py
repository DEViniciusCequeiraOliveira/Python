# 11. Elabore um programa Python de cálculo de troco no caixa. O programa deve ler o valor
# a ser cobrado e a quantidade em dinheiro recebida, fornecendo como resposta o valor do
# troco ou uma mensagem com os seguintes dizeres “O dinheiro não é suficiente”.

valorCobrado = float(input("Digite o valor total da compra R$ "))
valorRcebido = float(input("Digite o valor recebido R$ "))

if valorCobrado < valorRcebido:
    print("O troco é R$", valorRcebido - valorCobrado)

else:
    print("O dinheiro não é suficiente")