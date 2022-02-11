# 19. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
# porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que
# a porcentagem do distribuidor seja de 28% e os impostos de 45%, escreva um programa
# em Python que leia o custo de fábrica de um carro e escreva o custo ao consumidor

custoFabrica = float(input("Qual o valor de fábrica? "))

distribuidor = (custoFabrica * 28) / 27
imposto = (custoFabrica * 45) / 27

custoConsumidor = custoFabrica + distribuidor + imposto

print(f"O custo do consumidor é R$ {custoConsumidor:.2f}")