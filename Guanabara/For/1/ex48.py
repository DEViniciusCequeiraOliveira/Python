soma=0

for num in range(1,501,2):
    if num % 3 ==0:
        soma += num

print(f"A soma dos valores são: {soma}")