# Fazer um programa que leia 15 valores reais e os armazene em um vetor/estrutura B. Seu programa deverá
# passar o vetor para a função extremos. A função “extremos” deverá encontrar as posições onde estão o
# maior e o menor valor existente no vetor. A função principal deverá imprimir o maior e o menor valor bem como
# as respectivas posições no vetor.

def extremos(vetor):
    maiorValor = max(vetor)
    menorValor = min(vetor)
    posMaiorValor = vetor.index(maiorValor)
    posMenorValor = vetor.index(menorValor)
    return maiorValor, menorValor, posMaiorValor, posMenorValor

valores = []

for i in range(15):
    valor = int(input("Digite um valor: "))
    valores.append(valor)

a = extremos(valores)

print(f"O maior valor é {a[0]} e está na posição {a[2]}\n"
      f"O menor valor é {a[1]} e está na posição {a[3]}")