valores = []
posMaior = []
posMenor = []


for c in range(0,5):
    valores.append(int(input("Digite um número: ")))

maior = max(valores)
menor = min(valores)

for n, valor in enumerate(valores):
    if valor == maior:
        posMaior.append(n)

    if valor == menor:
        posMenor.append(n)

print(f"O maior número é {maior} e o menor é {menor}. O maior valor é na posição {posMaior} e a menor é na {posMenor}")