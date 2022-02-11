# 3. Escreve um programa em Python que solicite três números e informe se eles podem
# formar os lados de um triângulo.

a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))

ab = a+b
ac = a+c
bc = b+c

if ab > c and ac > b and bc > a:
    print("Esse trinâgulo existe!!!")

else:
    print("Esse trinâgulo não existe :(")