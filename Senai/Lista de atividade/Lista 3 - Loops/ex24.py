# 24. Escreva um programa em Python que calcule e apresente na tela a área de cada
# círculo através da fórmula A = PI * R * R, onde R (o valor que deverá ser digitado pelo
# usuário) representa o raio do círculo e PI é o número 3,14. Repetir o processo enquanto R
# for maior que 0.
from math import pi

raio = float(input("Digite o valor do raio: "))

while raio > 0:
    area = pi * raio ** 2
    print(f"A área do circulo é {area:.2f} m²")
    raio = float(input("\n o valor do raio: "))

print("\nFim do programa!")