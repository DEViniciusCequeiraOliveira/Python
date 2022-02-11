num = int(input("Digite um número: "))
cont = 0

for n in range(1,num + 1):
    if num % n == 0:
        cont += 1

if cont > 2:
    print("Não é primo")

else:
    print("É primo")