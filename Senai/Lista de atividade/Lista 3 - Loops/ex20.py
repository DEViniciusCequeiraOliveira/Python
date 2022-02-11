# 20. Em uma faculdade foram entrevistados 500 alunos. De cada um deles foram colhidas
# as seguintes informações: o código do curso que frequenta (1-engenharia; 2-computação;
# 3-matemática) e a idade. Faça um programa em Python que processe estes dados e que
# forneça as seguintes informações:
#         a) número de alunos por curso;
#         b) número de alunos com idade entre 20 e 25 anos, por curso;
#         c) o curso com o aluno mais velho e a idade deste aluno, e
#         d) o curso com menor média de idade.

def somaIdade(listaIdades):
    totalIdade = 0
    for idade in listaIdades:
        totalIdade += idade
    return totalIdade

def idade20Ate25(listaIdades):
    idade2025 = 0
    for idade in listaIdades:
        if idade > 20 and idade < 25:
            idade2025 += 1
    return idade2025

def mediaIdades(idadeEng,idadeComp,idadeMat):
    mediaEng = somaIdade(idadeEng) / len(idadeEng)
    mediaComp = somaIdade(idadeComp) / len(idadeComp)
    mediaMat = somaIdade(idadeMat) / len(idadeMat)
    return mediaEng, mediaComp, mediaMat

idadesEng = []
idadesComp = []
idadesMat = []

for i in range(5):
    codigoCurso = int(input("\nCódigo dos cursos: "
                            "\n1-Engenharia"
                            "\n2-Computação"
                            "\n3-Matemática"
                            "\nDigite o código: "))

    idadeAluno = int(input("\nDigite a sua idade: "))

    if codigoCurso == 1:
        idadesEng.append(idadeAluno)

    elif codigoCurso == 2:
        idadesComp.append(idadeAluno)

    elif codigoCurso == 3:
        idadesMat.append(idadeAluno)

idade20Eng25 = idade20Ate25(idadesEng)
idade20Comp25 = idade20Ate25(idadesComp)
idade20Mat25 = idade20Ate25(idadesMat)

maiorIdade = max(idadesMat,idadesComp,idadesMat)

media = mediaIdades(idadesEng,idadesComp,idadesMat)

print(f"No curso de Engenharia tem {len(idadesEng)} alunos")
print(f"No curso de Computação tem {len(idadesComp)} alunos")
print(f"No curso de Matemática tem {len(idadesMat)} alunos")

print(f"\nNo curso de Engenharia tem {idade20Eng25} alunos com mais de 20 e menos de 25")
print(f"No curso de Computação tem {idade20Comp25} alunos com mais de 20 e menos de 25")
print(f"No curso de Matemática tem {idade20Mat25} alunos com mais de 20 e menos de 25")

if maiorIdade in idadesMat:
    print("O aluno mais velho é de matemática")

elif maiorIdade in idadesComp:
    print("O aluno mais velho é de computação")

elif maiorIdade in idadesEng:
    print("O aluno mais velho é de engenharia")

cursoMinimo = {0:"Engenharia", 1:"Computação", 2:"Matemática"}

print(f"O curso com menor média de idade é {cursoMinimo[media.index(min(media))]} com média de {min(media)}")