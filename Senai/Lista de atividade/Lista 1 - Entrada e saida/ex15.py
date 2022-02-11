# 15. Faça um programa em Python para converter um dado valor em reais (R$) para a
# moeda dólar (US$). O programa deve ler um valor em reais (R$) e a cotação da moeda
# americana, depois converter para dólares (US$) e apresentar este valor convertido na tela.

real = float(input("Qual o valor em R$? "))

conversor = 5.64
dolar = conversor * real

print(f"O valor é U$ {dolar:.2f}")