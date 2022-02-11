# 20. Um fabricante paga uma porcentagem de imposto sobre o total de uma venda
# realizada. Esse fabricante conhece a quantidade de unidades de um produto que produziu
# e o valor de cada peça. Ajude este fabricante escrevendo um programa em Python que
# permita a leitura das seguintes informações: quantidade de unidades de um produto
# produzidas, valor (preço) de uma unidade desse produto e porcentagem de imposto a ser
# paga. Depois calcule o valor do imposto a ser pago e imprima na tela esse valor obtido.

qntVendida = int(input("Quantas unidades foram vendidas? "))
valorUnidade = float(input("Qual foi o valor vendido em R$ "))
porImposto = float(input("Quantos % de imposto? "))

valorTotal = qntVendida * valorUnidade
valorImposto = valorTotal * (porImposto) / 100

print(f"Vai ser pago R$ {valorImposto:.2f} de imposto")