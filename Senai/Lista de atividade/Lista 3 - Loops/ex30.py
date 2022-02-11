# 30. Professores preocupados com o número de faltas de seus alunos resolveram pedir
# para que esses alunos escrevessem um programa em Python para calcular a média de
# faltas dos alunos de uma determinada turma. Imagine que você é um aluno dessa turma e
# tem como tarefa escrever tal programa. Esse programa deve ler a quantidade de faltas dos
# alunos dessa turma (permitir a leitura enquanto for digitado um número positivo para a
# quantidade de faltas). Ao final imprimir a quantidade média de faltas e o número de alunos
# que participaram dessa pesquisa.

def somador(lista):
    soma = 0
    for n in lista:
        soma += n
    return soma

faltas =[]
faltaAluno = int(input("Digite quantas vezes esse aluno faltou: "))

while faltaAluno >= 0:
    faltas.append(faltaAluno)
    faltaAluno = int(input("Digite quantas vezes esse aluno faltou: "))

print(f"\nA média de faltas foi {(somador(faltas)/len(faltas)):.2f}")
print(f"Participaram da pesquisa {len(faltas)} alunos")

