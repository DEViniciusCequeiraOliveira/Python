# 13. Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada m2
# deve-se usar 18 W de potência. Escreva um programa em Python que leia as dimensões
# de um cômodo retangular (em metros), calcule e mostre a sua área (em m2
# ) e a potência
# de iluminação que deverá ser utilizada.

largura = float(input("Qual o seu largura em m? "))
comprimento = float(input("Qual o seu comprimento em m? "))

area = largura * comprimento

potencia = 18 * area

print(f"A sua área é {area:.2f} m² e precisa de {potencia:.2f} W")