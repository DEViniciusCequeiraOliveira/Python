 # 1. Escreva um programa que de acordo com o dia da semana digitado, informa quantas horas Seu Madruga trabalhou naquele dia.
# → Os dias da semana são representados pelos números de 1 (domingo) a 7 (sábado).
# → Às segundas, quartas e sextas, ele trabalha 8 horas por dia.
# → Às terças e quintas, ele trabalha 10 horas por dia.
# → Aos sábados e domingos, ele não trabalha (0 horas).
# → Ao final, mostre quantas horas ele trabalhou no dia indicado.
#  → Se um número inválido for informado (por exemplo: 8), exiba apenas uma mensagem de erro.

dia = input("Escolha o dia da semana para saber quanto seu Madruga trabalha: \n 1) DOM \n 2) SEG \n 3) TER \n 4) QUA \n 5) QUI \n 6) SEX \n 7) SAB \n")


if dia == "1":
  print("Ele trabalhou 0 hora")

elif dia == "2":
  print("Ele trabalhou 8 hora")
  
elif dia == "3":
  print("Ele trabalhou 10 hora")

elif dia == "4":
  print("Ele trabalhou 8 hora")

elif dia == "5":
  print("Ele trabalhou 10 hora")

elif dia == "6":
  print("Ele trabalhou 8 hora")

elif dia == "7":
  print("Ele trabalhou 0 hora")

else:
  print("Opção invalida")



 