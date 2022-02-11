# 7. Escreva um programa em Python que imprime todos os números primos entre 1 e n,
# onde n é fornecido pelo usuário

n = int(input("Digite o número final: "))


for num in range(2, n+1):
    primo = True

    for divisor in range(2, num):
        if num % divisor == 0:
            primo = False
            break

    if primo:
        print(num, "é primo!!!")