maior = 0
menor = 0


for _ in range(0,7):
    ano = int(input("Qual o seu ano de nascimeno? "))
    idade = 2021 - ano

    if idade > 20:
        maior += 1

    else:
        menor += 1

print(f"Tem {maior} maior de idade e {menor} menor de idade")