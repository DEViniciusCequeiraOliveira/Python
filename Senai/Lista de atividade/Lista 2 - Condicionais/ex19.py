# 19. Escreva um programa em Python que determina a data cronologicamente maior de
# duas datas fornecidas pelo usuário. Cada data deve ser fornecida por três valores inteiros
# onde o primeiro representa um dia, o segundo um mês e o terceiro um ano.

dia1 = int(input("Qual foi o dia: "))
mes1 = int(input("Qual foi o mês: "))
ano1 = int(input("Qual foi o ano: "))

dia2 = int(input("\nQual foi o outro dia: "))
mes2 = int(input("Qual foi o outro mês: "))
ano2 = int(input("Qual foi o outro ano: "))

if ano1 > ano2:
    print(f"O dia {dia1}/{mes1}/{ano1} é mais recente")
elif ano2 > ano1:
    print(f"O dia {dia2}/{mes2}/{ano2} é mais recente")

else:
    if mes1 > mes2:
        print(f"O dia {dia1}/{mes1}/{ano1} é mais recente")
    elif mes2 > mes1:
        print(f"O dia {dia2}/{mes2}/{ano2} é mais recente")
    else:
        if dia1 > dia2:
            print(f"O dia {dia1}/{mes1}/{ano1} é mais recente")
        elif dia2 > dia1:
            print(f"O dia {dia2}/{mes2}/{ano2} é mais recente")
        else:
            print("Os datas são iguais.")