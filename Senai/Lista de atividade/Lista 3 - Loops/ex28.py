# 28. Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados
# de idade e quantidade de filhos. Faça um programa em Python que informe:
#          a média de idade do grupo;
#          quantidade de pessoas com mais de 5 filhos;
#          porcentagem de pessoas com menos de 20 anos e com filhos;
#          quantidade de pessoas entrevistadas;
# O programa finalizará a leitura dos dados quando for digitado um valor negativo para a
# idade.

def somador(valorLista):
    somaValor = 0
    for valor in valorLista:
        somaValor += valor
    return somaValor

def maisCinco(listaFilho):
    cont = 0
    for filho in listaFilho:
        if filho > 5:
            cont += 1
    return cont

def filhoComVinte(listaIdade,listaFilho):
    cont = 0
    for idade,filho in zip(listaIdade,listaFilho):
        if filho > 0 and idade < 20:
            cont += 1
    return cont

def temFilho(listaFilho):
    cont = 0
    for filho in listaFilho:
        if filho > 0:
            cont += 1
    return cont

idades = []
filhos = []

for i in range(10):
    idade = int(input("Digite a sua idade: "))
    qntFilho = int(input("Digite a quantidade de filhos: "))

    idades.append(idade)
    filhos.append(qntFilho)

print(f"\nA média de idade é {somador(idades) / len(idades)}")
print(f"Existe {maisCinco(filhos)} pessoa com mais de 5 filhos")
print(f"{((filhoComVinte(idades,filhos) * 100)/(temFilho(filhos))):.2f}% tem filhos com menos de 20 anos")
print(f"Foram entrevistados {len(idades)} pessoas")