# 10. Faça uma função que receba estrutura de dados com 10 números e informe a quantidade de
# ocorrências do último número lido. Por exemplo, para a sequência 38 4 23 5 6 7 4 12 4, o resultado
# deve ser ‘O número 4 apareceu 3 vezes’.

def funcao():
    num = 0
    lista = []
    for i in range(10):
        num = int(input("digite: "))
        lista.append(num)

  print(lista)
  print(f"O número {lista[-1]} apareceu {lista.count(lista[-1])} vezes")