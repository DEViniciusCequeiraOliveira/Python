# 21. Uma fábrica tem um vendedor que recebe uma comissão calculada a partir do número
# de itens de um pedido, segundo os seguintes critérios:
#          para pedidos com menos de 20 itens, a comissão é de 10% do valor total do pedido;
#          para pedidos de 20 a 49 itens, a comissão é de 15% do valor total do pedido;
#          para pedidos de 50 a 74 itens, a comissão é de 20% do valor total do pedido;
#          para pedidos iguais ou superiores a 75 itens, a comissão é de 25%.
# Escreva um programa em Python que processe N pedidos vinculados a esse vendedor (N
# deve ser lido, portanto). Para cada pedido o programa deve ler a quantidade de itens
# vendidos e o valor total. O programa deve informar:
#          A soma total das comissões;
#          A média de itens vendidos;
#          Porcentagem de pedidos com menos de 20 itens.

def somaComissao(valoresComissao):
    soma = 0
    for n in valoresComissao:
        soma += n
    return soma

valoresComissaoBaixa = []
valoresComissaoMedia = []
valoresComissaoAlta = []
valoresComissaoAltissima = []

somaItem = 0

pedidos = int(input("Quantos pedidos foram vendidos: "))
for i in range(pedidos):
    item = int(input("\nDigite a quantidade de itens: "))
    valorTotal = float(input("Digite o valor total em R$ "))
    if item > 0 and item <= 20:
        valoresComissaoBaixa.append(valorTotal * 0.1)

    elif item > 20 and item < 49:
        valoresComissaoMedia.append(valorTotal * 0.15)

    elif item >= 50 and item < 74:
        valoresComissaoAlta.append(valorTotal * 0.2)

    elif item >= 75:
        valoresComissaoAltissima.append(valorTotal * 0.25)

    somaItem += item

valoresComissao = valoresComissaoBaixa + valoresComissaoMedia + valoresComissaoAlta + valoresComissaoAltissima

print(f"\nA soma das comissões é R$ {somaComissao(valoresComissao)}")
print(f"A média de itens vendidos são {(somaItem/pedidos):.2f}")
print(f"A porcentagem de pedidos com menos de 20 itens {((len(valoresComissaoBaixa) * 100)/pedidos):.2f}%")

