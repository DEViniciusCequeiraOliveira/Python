# 22. Um aluno deseja saber qual a porcentagem de faltas que ele tem em cada disciplina.
# Ajude este aluno para que ele sempre possa calcular sua porcentagem de faltas. Para
# isso, escreva um programa em Python que leia a carga horária da disciplina e a
# quantidade de horas de faltas acumuladas, calcule a porcentagem e a imprima na tela.

cargaHoraria = int(input("Qual a carga horária na matéria em horas? "))
faltaAcumulada = int(input("Qual a quantidade em horas de falta acumulada? "))

porFalta = (faltaAcumulada * 100) / cargaHoraria

print(f"Ele faltou {porFalta:.2f}% de horas")