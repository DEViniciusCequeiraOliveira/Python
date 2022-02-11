# 6. Faça um programa em Python que leia 4 números e informe quantos são maiores que
# 10. Use somente duas variáveis.

# nums = []
# count = 0
#
# for _ in range(0, 4):
#     nums.append(float(input("Digite um número: ")))
#
# for num in nums:
#     if num > 10:
#         count += 1
#
# print(f"Existe {count} números maior que 10")

count = 0

num = float(input("Digite um número: "))
if num > 10:
    count += 1

num = float(input("Digite um número: "))
if num > 10:
    count += 1

num = float(input("Digite um número: "))
if num > 10:
    count += 1

num = float(input("Digite um número: "))
if num > 10:
    count += 1

print(f"Existe {count} números maior que 10")