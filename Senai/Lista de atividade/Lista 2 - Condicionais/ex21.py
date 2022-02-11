# 21. Escreva um programa em Python que determina quanto tempo (segundos) um corpo
# leva para cair de uma determinada altura (h0 0), dada em metros (m), a partir do repouso
# (v0 = 0). Lembre-se que h = h0 + v0t + (gt2)/2. Assuma: h = 0, g = - 9,8 m/s2
# . Use a função
# sqrt (x), da biblioteca math, para obter a raiz quadrada. Seu programa deve pedir que o
# usuário informe h0 e adverti-lo caso o valor informado seja negativo.
from math import sqrt

h0 = float(input("Digite o h0 em m: "))

if h0 >= 0:
    tempo = sqrt((2 * h0)/9.8)
    print(f"O tempo da queda foi de {tempo:.2f} segundos")

else:
    print("Não aceitamos números negativos")