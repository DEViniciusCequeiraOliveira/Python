# 22. Escreva um programa em Python que leia a quantidade de pessoas entrevistadas. Em
# seguida, para cada pessoa leia a idade e o sexo e calcule e mostre:
#          A média de idade das pessoas;
#          A média de idade das mulheres;
#          A média de idade dos homens;
#          A quantidade de pessoas em cada faixa etária segundo a tabela a seguir;
#             Faixa Etária Idade
#                 1 Até 15 anos
#                 2 De 16 a 30 anos
#                 3 De 31 a 45 anos
#                 4 De 46 a 60 anos
#                 5 Acima de 60 anos
#          A porcentagem de mulheres da segunda faixa etária.
faixaEtaria1 = []

def somador(lista):
    somaElemento = 0
    for elemento in lista:
        somaElemento += elemento
    return somaElemento

def faixaEtaria(listaIdade):
    for idade in listaIdade:
        if idade > 15 and idade <= 30:
            faixaEtaria1.append(idade)
    return faixaEtaria1

idadeMasculino = []
idadeFeminino = []

candidato = int(input("Digite a quantidadde de candidatos: "))
for i in range(candidato):
    idade = int(input("Digite a idade: "))
    sexo = int(input("1- Homem\n2- Mulher\n"))

    if sexo == 1:
        idadeMasculino.append(idade)

    elif sexo == 2:
        idadeFeminino.append(idade)

idadeGeral = idadeFeminino + idadeMasculino

print(f"A média de idade das pessoas é {(somador(idadeGeral))/(candidato)}")
print(f"A média da idade das mulheres é {(somador(idadeFeminino))/(len(idadeFeminino))}")
print(f"A média de idade dos homens é {(somador(idadeMasculino))/(len(idadeMasculino))}")
print(f"A porcentagem de mulheres da segunda faixa etária {((len(faixaEtaria(idadeFeminino)) * 100) / (len(idadeFeminino))):.2f}% ")
