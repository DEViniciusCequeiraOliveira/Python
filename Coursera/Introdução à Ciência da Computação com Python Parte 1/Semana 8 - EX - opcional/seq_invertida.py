numeros = []

numero = int(input("Digite um número: "))

while numero !=0:
    numeros.append(numero)
    numero = int(input("Digite um número: "))

numeros.reverse()

for n in numeros:
    print(n)