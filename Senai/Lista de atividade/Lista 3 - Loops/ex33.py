# 33. Considere um cinema a respeito do qual foi feita uma pesquisa de qualidade. Certo
# dia, cada espectador respondeu a um questionário, no qual constava sua opinião em
# relação ao filme, segundo as seguintes notas:
#     Nota Significado
#         1 Ótimo
#         2 Regular
#         3 Ruim
#     Elabore um programa em Python que, lendo esse dado fornecido pelos espectadores,
#     calcule e imprima:
#          A quantidade de pessoas que participaram da pesquisa;
#          A porcentagem de respostas “ótimo” (notas 1);
#          A porcentagem de respostas “regular” (notas 2);
#          A porcentagem de respostas “ruim” (notas 3).
# Quando for digitada uma nota inválida, significa que a digitação dos dados chegou ao fim.

def notasPorcentagem(nota, listaNotas):
    somador = 0
    for n in listaNotas:
        if n == nota:
            somador += 1
    return somador

def porcentagem (qnt):

    porcent = (100 * qnt) / len(notasGerais)
    return porcent

notasGerais = []

nota = int(input("Digite sua nota: "))

while nota >= 1 and nota <= 3:
    notasGerais.append(nota)
    nota = int(input("Digite sua nota: "))

nota1 = notasPorcentagem(1, notasGerais)
nota2 = notasPorcentagem(2, notasGerais)
nota3 = notasPorcentagem(3, notasGerais)

print(f"Participaram da pesquisa {len(notasGerais)} pessoas")
print(f"A porcentagem de resposta ótima foi {porcentagem(nota1)}%")
print(f"A porcentagem de resposta regular foi {porcentagem(nota2)}%")
print(f"A porcentagem de resposta ruim foi {porcentagem(nota3)}%")
