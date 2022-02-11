# O produto entre dois números inteiros sempre pode ser calculado utilizando-se apenas o operador de
# adição. Assim: 2 * 3 = 2 + 2 + 2 Ou seja: x * y = x + x + ...+ x (y vezes). Escreva uma função recursiva
# para o cálculo do produto  de dois números, usando apenas o operador de soma.

def multiplicador(num1, num2):
    if num1 == 1:
        return num2
    else:
        num1 -= 1
        return num2 + multiplicador(num1,num2)


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = multiplicador(num1,num2)

print(f"\n{num1} X {num2} = {resultado}")