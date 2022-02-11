# 24. Um serviço de entrega em domicílio cobra 4 reais para fazer qualquer entrega mais um
# acréscimo por quilômetro dependente da distância (d) até o local da entrega, de acordo
# com a tabela a seguir:
# Distância (Km) Acréscimo por quilômetro
# 0 <= d <= 3 0,50
# 3 < d <= 6 0,75
# d > 6 1,00
# Escreva um programa em Python que leia a distância em quilômetros da origem até o
# destino e calcule e imprima na tela o valor a ser pago. Por exemplo: se a entrega for a 5
# quilômetros de distância, a pessoa irá pagar: 4 + 5*0,75 = 7,75.

distancia = float(input("Digite a distância em Km da origem até o destino final: "))

if distancia >= 0 and distancia <= 3:
    valor = 4 + 0.5 * distancia
    print(f"O valor da entrega é R$ {valor:.2f}")

elif distancia > 3 and distancia <= 6:
    valor = 4 + 0.75 * distancia
    print(f"O valor da entrega é R$ {valor:.2f}")

elif distancia > 6:
    valor = 4 + 1 * distancia
    print(f"O valor da entrega é R$ {valor:.2f}")

else:
    print("Distância não válida !!!")