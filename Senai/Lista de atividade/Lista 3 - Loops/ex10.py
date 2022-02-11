# 10. Faça um programa em Python que leia 10 valores, um de cada vez, e calcule a média,
# mostrando o resultado ao final.
somaNum = 0

for c in range(0,10):
    num = int(input("Digite um número: "))
    somaNum += num

media = somaNum / 10

print("Sua média é", media)