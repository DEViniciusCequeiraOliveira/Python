# 23. Um hotel com 80 apartamentos deseja fazer uma promoção especial de final de
# semana, concedendo um desconto de 25% na diária. Com isto, espera aumentar sua taxa
# de ocupação de 50% para 80%. Sendo dado o valor normal da diária, escreva um
# programa em Python que calcule e imprima:
# a) o valor da diária promocional;
# b) valor total arrecadado com 80% de ocupação e diária promocional;
# c) o valor total arrecadado com 50% de ocupação e diária normal;
# d) a diferença entre estes dois valores.
# Exemplo:
# Se for digitado o valor de 50 reais para a diária normal devemos imprimir na tela:
# Diária promocional = 37.5
# Total arrecadado com 80% de ocupação e diária promocional = 2400
# Total arrecadado com 50% de ocupação e diária normal = 2000
# Diferença entre os valores: 400

valorDiaria = float(input("O valor da diária é? "))

valorDiariaDescontado = valorDiaria * 75 / 100
totalArrecadado80 = 80 * (80)/(100) * valorDiariaDescontado
totalArrecadado50 = 80 * (50)/(100) * valorDiariaDescontado

print(f"A diária promocioanl é R$ {valorDiariaDescontado:.2f} e total arrecadado com 80% é R${totalArrecadado80:.2f}"
      f" e o total com 50% é R$ {totalArrecadado50:.2f}")