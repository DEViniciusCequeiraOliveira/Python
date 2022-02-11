# 27. Escreva um programa em Python que leia um número indeterminado de notas entre
# 0.0 e 10.0. Ao final imprima a quantidade de notas maiores ou iguais a 7. A digitação deve
# ser encerrada quando for digitada uma nota inválida.

notasAprovados = []

nota = float(input("Digite a nota: "))

while nota <= 10 and nota >= 0:
    if nota >= 7:
        notasAprovados.append(nota)

    nota = float(input("Digite a nota: "))

print(f"{len(notasAprovados)} alunos foram aprovados")