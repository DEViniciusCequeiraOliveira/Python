# Escreva um programa em Python que, dadas as dimensões das figuras apresentadas
# (lidas do teclado) calcule o volume e a área da Superfície de cada um. Primeiro o usuário
# vai entrar com os lados do paralelepípedo, então programa já pode mostrar o volume e a
# área desta figura. Depois entra com a área da base e altura do cilindro, obtendo a resposta
# e por fim entra com o raio da esfera e o programa faz o último cálculo.
from math import pi
from math import pow


ladoA = float(input("Digite o valor do lado A do Paralelepípedo: "))
ladoB = float(input("Digite o valor do lado B do Paralelepípedo: "))
ladoC = float(input("Digite o valor do lado C do Paralelepípedo: "))

volumeParalelepipedo = ladoA * ladoB * ladoC
areaParalelepipedo = 2 * (ladoA*ladoB + ladoB*ladoC + ladoC*ladoA)



alturaCilindro = float(input("\nDigite o valor da altura do Cilindro: "))
raioCilindro = float(input("Digite o valor do raio do Cilindro: "))

volumeCilindro = alturaCilindro * pow(raioCilindro, 2) * pi
areaCilindro = 2 * (pow(raioCilindro, 2) * pi) + (2 * pi * raioCilindro)



raioEsfera = float(input("\nDigite o valor do raio da Esfera: "))

volumeEsfera = (4 * pi * pow(raioEsfera, 3))/(3)
areaEsfera = 4 * pi * pow(raioEsfera, 2)



print(f"\nO volume do Paralelepípedo é {volumeParalelepipedo} e área da superfície é {areaParalelepipedo}\n"
      f"O volume do Cilindro é {volumeCilindro:.2f} e área da superfície é {areaCilindro:.2f}\n"
      f"O volume do Esfera é {volumeEsfera:.2f} e área da superfície é {areaEsfera:.2f}")