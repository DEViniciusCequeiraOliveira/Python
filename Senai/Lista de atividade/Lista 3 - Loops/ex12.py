# 12. Calcule a raiz quadrada de um número inteiro positivo sem usar a função sqrt. Para
# isso, você precisa saber que a raiz quadrada de um número N é igual à quantidade de
# números ímpares consecutivos (a partir do 1) cuja soma é igual a N (ou o mais próxima
# possível de N). Ou melhor, exemplificando:
# Qual a raiz quadrada de 16? 1 + 3 + 5 + 7 = 16
#  4 números ímpares consecutivos foram somados. Então 4 é a raiz quadrada de
# 16.
# Qual a raiz quadrada de 25? 1 + 3 + 5 + 7 + 9 = 25
#  5 números ímpares consecutivos foram somados. Então 5 é a raiz quadrada de
# 25.
# Qual a raiz quadrada de 36? 1 + 3 + 5 + 7 + 9 + 11 = 36
#  6 números ímpares consecutivos foram somados. E 6 é a raiz quadrada de 36.
# Qual a raiz quadrada de 30? A raiz quadrada inteira de 30 é 5 (aproximando para
# baixo), porque 25 < 30 < 36, logo a parte inteira da raiz quadrada de 30 é igual à raiz
# quadrada de 25.


num = int(input("Digite um número: "))

impar = 1
raizCont = 0
soma = 0

while soma < num:
    impar += 2
    soma += impar
    raizCont += 1

print("A raiz é", raizCont)
