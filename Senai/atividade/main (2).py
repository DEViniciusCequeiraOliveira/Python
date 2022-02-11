# 2. Escreva um programa que pede o ano de nascimento da pessoa e mostra em qual ciclo de ensino ela deve estudar.
# → Caso a pessoa tenha entre 2 e 5 anos, deve estar no Infantil.
# → Caso a pessoa tenha entre 6 e 10 anos, deve estar no Fund I.
# → Caso a pessoa tenha entre 11 e 14 anos, deve estar no Fund II.
# → Caso a pessoa tenha entre 15 e 17 anos, deve estar no Médio.
# → Caso a pessoa tenha outra idade, o ciclo não é detectado.
# → Por fim, o ciclo de ensino atual é exibido.


ano_nasc = int(input("Informe o ano de nascimento da criança: "))

idade = 2021 - ano_nasc

if idade >=2 and idade <= 5:
  print("Ciclo de ensino atual: Ensino infantil")

elif idade >= 6 and idade <=10:
  print("Ciclo de ensino atual: Ensino Fundamental I")

elif idade >=11 and idade <= 14:
  print("Ciclo de ensino atual: Ensino Fundamental II")

elif idade >= 15 and idade <= 17:
  print("Ciclo de ensino atual: Ensino Médio")

else:
  print("Ciclo não detectado")