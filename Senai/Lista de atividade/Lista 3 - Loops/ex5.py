# 5. Escreva um programa em Python que lê uma sequência de números inteiros e imprime
# qual o maior e qual o menor valor dessa seqüência. A seqüência termina com o número 0
# (zero).
nums = []
num = 1

while num != 0:
    num = float(input("Digite um número: "))
    if num !=0:
        nums.append(num)

maiorNum = max(nums)
menorNum = min(nums)

print(f"O maior número é {maiorNum} e o menor é {menorNum}")