# 3. Escreva um programa que sugere o modo de transporte da pessoa de acordo com a distância até o destino e a disponibilidade de dinheiro. 
# → Inicialmente, o programa pede para a pessoa informar a distância (em km) até o destino. Se um número inválido (0 ou menos) for digitado, o programa é encerrado.
# → Mas se uma distância válida for informada, então o programa pergunta se a pessoa tem dinheiro para o trajeto.
# → Caso a pessoa digite S (para “Sim”), o programa verifica:
# → Para distância de até 500 km, sugere ir de ônibus.
# → Caso contrário, sugere ir de avião.
# → Caso a pessoa digite uma resposta diferente de S, então:
# → Para distância de até 3 km, sugere ir a pé.
# → Para distância acima de 3 km e até 20 km, sugere ir de bike.
# → Caso contrário, sugere ir de carona.

distancia = float(input("Informe a distancia (em Km): "))

if distancia <= 0:
  print("Tá de sacanagem? ")

else:
  dinheiro = input("Você tem dinheiro? S para sim: ")

  if distancia <= 500 and dinheiro == "S":
    print("Vá de ônibus! ") 

  elif distancia > 500 and dinheiro == "S":
    print("Vá de avião! ")

  elif distancia <= 3:
    print("Vá a pé! ")
  
  elif distancia >3 and distancia <=20:
    print("Vá de Bike! ")
  
  else:
    print("Vá de carona! ")
  
 