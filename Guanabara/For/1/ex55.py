menor = 0
maior = 0

for p in range(0,5):
    peso = float(input("Qual o peso em Kg "))

    if p == 0:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso

        elif menor > peso:
            menor = peso

print(f"O maior peso é {maior} Kg e menor peso é {menor} Kg")