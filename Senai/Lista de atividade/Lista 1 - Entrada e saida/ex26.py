# 25. Faça um programa em Python que solicite ao usuário a nota de suas 3 provas e
# imprima a média aritmética delas.
# 26. Repita o exercício anterior usando apenas duas variáveis.
somaNota = 0

for _ in range(0,3):
    nota = float(input("Qual a sua nota: "))
    somaNota = somaNota+ nota

print(f"A sua média é: ", somaNota / 3)