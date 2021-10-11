import math

a = int(input("O valor de a: "))
b = int(input("O valor de b: "))
c = int(input("O valor de c: "))

delta = b**2 - 4 * a * c



if delta < 0:
  print("esta equação não possui raízes reais")

else:

  raiz1 = (-b + math.sqrt(delta)) / (2 * a)
  raiz2 = (-b - math.sqrt(delta)) / (2 * a)

  if delta == 0:
    print(f"a raiz desta equação é {raiz1}")

  elif delta > 0:
    if raiz1 > raiz2:  #Comando para exebir primeiro a raiz menor
      print(f"as raízes da equação são {raiz2} e {raiz1}")

    else:
      print(f"as raízes da equação são {raiz1} e {raiz2}")
