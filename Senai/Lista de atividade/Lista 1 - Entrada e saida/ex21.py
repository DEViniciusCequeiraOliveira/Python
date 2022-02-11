# 21. Faça um programa em Python que leia a idade de uma pessoa expressa em anos,
# meses e dias e mostre-a expressa apenas em dias. Assuma, neste programa, que um ano
# tem 365 dias e que um mês tem 30 dias. Exemplo: Se a pessoa digitar que tem 28 anos 1
# mês e 10 dias deverá aparecer na tela que ela viveu 10260 dias.

anos = int(input("Quantos anos tem? "))
meses = int(input("Quantos mesês tem? "))
dias = int(input("Quantos dias tem? "))

anosToDias = anos * 365
mesesToDias = meses * 30

diasTotal = anosToDias + mesesToDias + dias

print(f"Você viveu {diasTotal} dias")