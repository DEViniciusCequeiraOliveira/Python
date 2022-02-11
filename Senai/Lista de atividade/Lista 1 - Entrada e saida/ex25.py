# 25. Faça um programa em Python que solicite ao usuário a nota de suas 3 provas e
# imprima a média aritmética delas.

nota1 = float(input("Qual a sua nota em Matématica? "))
nota2 = float(input("Qual a sua nota em Química? "))
nota3 = float(input("Qual a sua nota em Física? "))

media = (nota1 + nota2 + nota3) / 3

print(f"Sua média é: {media:.2f}")