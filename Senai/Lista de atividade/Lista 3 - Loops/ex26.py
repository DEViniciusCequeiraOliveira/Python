# 26. Adaptar o programa desenvolvido acima para que ela calcule o percentual dos valores
# positivos e negativos em relação ao total de valores fornecidos.

contPos = 0
contNeg = 0

n = int(input("Digite um número: "))

while n !=0:
    if n > 0:
        contPos +=1

    elif n < 0:
        contNeg +=1
    n = int(input("Digite um número: "))


print(f"Teve {contPos} ({((contPos * 100)/(contNeg + contPos)):.2f}%) números positivos e {contNeg} ({((contNeg * 100) / (contNeg + contPos)):.2f}%) números negativos")