# 23. Escreva um programa em Python que leia as 50 notas de uma avaliação dos alunos
# que cursam uma disciplina de algoritmos, calcule e imprima na tela:
#          a quantidade de notas maiores ou iguais a 7;
#          a porcentagem de notas maiores ou iguais a 7;
#          quantidade de notas maiores ou iguais a 4 e menores que 7;
#          a porcentagem de notas maiores ou iguais a 4 e menores que 7;
#          quantidade de notas menores que 4;
#          a porcentagem de notas menores que 4;
#          a média da turma na avaliação.

notaAprovado = []
notaRecuperacao = []
notaReprovado = []
somaNota = 0

for i in range(5):
    nota = int(input("Digite a nota: "))
    somaNota += nota

    if nota >= 7 and nota <= 10:
        notaAprovado.append(nota)

    elif nota >= 4 and nota < 7:
        notaRecuperacao.append(nota)

    elif nota >= 0 and nota < 4:
        notaReprovado.append(nota)

totalNotas = notaAprovado + notaRecuperacao + notaReprovado


print(f"\n{len(notaAprovado)} alunos foram aprovados")
print(f"{(len(notaAprovado) * 100) / len(totalNotas)}% dos alunos foram aprovados")
print(f"\n{len(notaRecuperacao)} alunos ficaram em recuperação")
print(f"{(len(notaRecuperacao) * 100) / len(totalNotas)}% dos alunos ficaram em recuperação")
print(f"\n{len(notaReprovado)} alunos foram reprovados")
print(f"{(len(notaReprovado) * 100) / len(totalNotas)}% dos alunos foram reprovados")
print(f"\n A média da turma foi {somaNota/len(totalNotas)}")

