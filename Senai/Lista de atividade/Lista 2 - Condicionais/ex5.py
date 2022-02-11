# 5. Faça um programa em Python que leia 4 números positivos e imprima o menor deles.
# Use somente duas variáveis.

nums = []

for c in range(0,4):
    num = float(input("Digite um número: "))
    nums.append(num)

nums.sort()

print("O menor número é", nums[0])