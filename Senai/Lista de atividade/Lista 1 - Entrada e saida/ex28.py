# 28. Escreva um programa em Python que, dados os valores a, b e c de uma equação
# quadrática ax2+bx+c = 0, calcule a maior das raízes que resolve a equação. Suponhamos
# que o valor calculado para delta é sempre positivo, ou seja, b2 > 4ac.
from math import pow

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = pow(b, 2) - 4 * a * c
raiz1 = (-b + delta) / (2*a)
raiz2 = (-b - delta) / (2*a)

print(f"Raiz 1 é {raiz1} e raiz 2 é {raiz2}")