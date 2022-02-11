# 18. Deseja-se fazer uma pesquisa a respeito do consumo mensal de energia elétrica em
# uma determinada cidade. Para isso são fornecidos os seguintes dados de 500
# consumidores:
#    quantidade de kWh consumidos durante o mês;
#    código do tipo de consumidor (1 - residencial, 2 - comercial, 3 - industrial).
# Calcular:
#   a) a média de consumo residencial;
#   b) a media de consumo comercial;
#   c) a média de consumo industrial;
#   d) o total de consumo para cada um dos tipos de consumidores;

residencial, residencialKWhTotal = 0,0
comercial, comercialKWhTotal = 0,0
industrial, industrialKWhTotal = 0,0


for i in range(5):
    print("1 - residencial"
          "\n2 - comercial"
          "\n3 - industrial\n")

    codigo = int(input("Digite o seu código de consumidor: "))


    if codigo == 1:
        residencialKWh = float(input("Consumiu quantos Kwh: "))
        residencial += 1
        residencialKWhTotal += residencialKWh

    elif codigo == 2:
        comercialKWh = float(input("Consumiu quantos Kwh: "))
        comercial += 1
        comercialKWhTotal += comercialKWh

    elif codigo == 3:
        industrialKWh = float(input("Consumiu quantos Kwh: "))
        industrial += 1
        industrialKWhTotal += industrialKWh


mediaResidencial = residencialKWhTotal / residencial
mediaComercial = comercialKWhTotal / comercial
mediaIndustrial = industrialKWhTotal / industrial

print(f"A média consumida pelas residencias foi de {mediaResidencial:.2f} Kwh e teve um total de {residencialKWhTotal} Kwh")
print(f"A média consumida pelos comercios foi de {mediaComercial:.2f} Kwh e teve um total de {comercialKWhTotal} Kwh")
print(f"A média consumida pelas residencias foi de {mediaIndustrial:.2f} Kwh e teve um total de {industrialKWhTotal} Kwh")