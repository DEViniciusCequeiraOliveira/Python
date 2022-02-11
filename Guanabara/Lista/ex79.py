resposta = str
valores = []
antigo = []

while resposta != "N" and resposta != "n":
    valor = int(input("Digite um valor: "))

    if valor not in valores:
        valores.append(valor)

    resposta = input("Deseja continuar? S/N ")

valores.sort()
print(valores)

