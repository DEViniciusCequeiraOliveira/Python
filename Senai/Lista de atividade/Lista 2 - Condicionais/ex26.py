# 26. Ajude um proprietário de cachorro a calcular quantos dias um pacote de ração pode
# durar. Escreva um programa em Python que leia o peso do cachorro em quilos e o peso da
# embalagem de ração em quilos, e calcule e imprima a quantidade de dias que o pacote de
# ração irá durar. A tabela abaixo indica a porção diária de acordo com a faixa de peso do
# cachorro:
# Peso do cachorro em Kg Porções diárias
#    Até 5 Kg                 60g
#    6 – 10 Kg                95g
#   11 – 15 Kg                135g
#   16 – 20 Kg                170g
#   Acima de 21 Kg            215g

pesoCachorro = float(input("Digite o peso do cachorro em Kg: "))
pesoRacao = float(input("Digite o peso da embalagem da ração em Kg: "))

if pesoCachorro > 0 and pesoCachorro <= 5:
    tempo = pesoRacao * 1000 // 60
    print(f"A ração vai durar {tempo} dias")

elif pesoCachorro >= 6 and pesoCachorro <= 10:
    tempo = pesoRacao * 1000 // 95
    print(f"A ração vai durar {tempo} dias")

elif pesoCachorro >= 11 and pesoCachorro <= 15:
    tempo = pesoRacao * 1000 // 135
    print(f"A ração vai durar {tempo} dias")

elif pesoCachorro >= 16 and pesoCachorro <= 20:
    tempo = pesoRacao * 1000 // 170
    print(f"A ração vai durar {tempo} dias")

elif pesoCachorro >= 21:
    tempo = pesoRacao * 1000 // 215
    print(f"A ração vai durar {tempo} dias")

else:
    print("Peso do cachorro digitado errado, por favor tente novamente!")