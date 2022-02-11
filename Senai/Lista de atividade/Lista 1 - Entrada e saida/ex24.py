# 24. Um sistema de máquinas demora 37 segundos para produzir uma peça. Sua tarefa é
# fazer um programa em Python que leia a quantidade de peças a ser produzida e calcule o
# tempo em horas, minutos e segundos necessário para produzir essa quantidade de peças.
# Exemplo: Se digitado pelo usuário a quantidade 250, deverá aparecer na tela 2 horas, 34
# minutos e 10 segundos.

qntPeca = int(input("Quantas peças foram produzidas? "))

tempProduzido = qntPeca * 37

horas = tempProduzido // 3600
restHoras = tempProduzido % 3600
minutos = restHoras // 60
restMinutos = restHoras % 60
segundos = restMinutos % 60

print(f"O tempo foi de {horas} horas, {minutos} minutos e {segundos} segundos")