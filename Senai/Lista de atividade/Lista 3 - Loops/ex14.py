# 14. Escreva um programa em Python que leia a nota final de um número indeterminado de
# alunos, e escreva na tela a situação de cada um. “APROVADO” se NF >= 7; “EM EXAME”
# se 4 <= NF < 7; “REPROVADO” se NF < 4. O programa deve ser encerrado se for digitada
# uma nota final fora do intervalo entre 0 e 10.
notaFinal = 0

while notaFinal >= 0 and notaFinal <= 10:
    notaFinal = float(input("Digite a sua nota final: "))
    if notaFinal >= 7 and notaFinal <= 10:
        print("APROVADO")

    elif notaFinal >= 4 and notaFinal < 7:
        print("EM EXAME")

    elif notaFinal >= 0 and notaFinal < 4:
        print("REPROVADO")

print("\nFim do programa!")