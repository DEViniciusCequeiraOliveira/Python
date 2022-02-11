# 29. A fábrica WK produz uma quantidade de automóveis por dia e deseja fazer um
# levantamento sobre essa produção. Escreva um programa em Python que leia a
# quantidade de automóveis produzida diariamente, enquanto não for digitado um número
# negativo. Ao final o programa deve mostrar na tela a quantidade total de automóveis
# produzida, a quantidade de dias que foi considerada (ou seja, é a quantidade de números
# digitados), e a quantidade média de carros produzida por dia.

def somador(lista):
    soma = 0
    for n in lista:
        soma += n
    return soma

automoveis = []
qntAutomoveis = int(input("Digite a quantidade de automóveis produzidos: "))

while qntAutomoveis >= 0:
    automoveis.append(qntAutomoveis)
    qntAutomoveis = int(input("Digite a quantidade de automóveis produzidos: "))

print(f"Foram produzidos {somador(automoveis)} automovéis em {len(automoveis)} dias")
print(f"Média de automoveis por dia foi: {(somador(automoveis)/len(automoveis)):.2f}")