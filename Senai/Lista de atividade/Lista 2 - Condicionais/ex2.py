# 2. O conceito de um estudante é calculado de acordo com a seguinte tabela:
# Nota: Maior ou igual a 9.0 → Conceito: A
# Nota: Menor que 9.0 mas maior ou igual a 8.0 → Conceito: B
# Nota: Menor que 8.0 mas maior ou igual a 7.0 → Conceito: C
# Nota: Menor que 7.0 mas maior ou igual a 6.0 → Conceito: D
# Nota: Menor que 6.0 → Conceito: F
# Implemente um programa em Python que receba a nota e devolva o conceito de um aluno.

nota = float(input("Digite a sua nota: "))

if nota < 10 and nota >= 9:
    print("Conceito A")

elif nota < 9 and nota >= 8:
    print("Conceito B")

elif nota < 8 and nota >= 7:
    print("Conceito C")

elif nota < 7 and nota >= 6:
    print("Conceito D")

elif nota > 6:
    print("Conceito F")