# 20. Escreva um programa em Python que solicita ao usuário duas datas (dia, mês, ano),
# onde a primeira data é o dia atual e a segunda é a data de vencimento de suas contas, em
# seguida o seu programa deve imprimir se a conta em questão “está atrasada”, “não está
# atrasada” ou “vence neste dia”. Assuma que o usuário informa duas datas válidas.

diaAtual = int(input("Digite o dia atual: "))
mesAtual = int(input("Digite o mês atual: "))
anoAtual = int(input("Digite o ano atual: "))

diaVenc = int(input("\nDigite o dia do vencimento: "))
mesVenc = int(input("Digite o mês do vencimento: "))
anoVenc = int(input("Digite o ano do vencimento: "))

if anoAtual > anoVenc:
    print("Não está atrasada")

elif anoAtual < anoVenc:
    print("Está atrasada")

else:
    if mesAtual > mesVenc and mesAtual <= 12 and mesVenc <= 12:
        print("Não está atrasada")

    elif mesAtual < mesVenc and mesAtual <= 12 and mesVenc <= 12:
        print("Está atrasada")

    else:
        if diaAtual < diaVenc and diaAtual <= 31 and diaVenc <= 31:
            print("Está atrasada")

        elif diaAtual > diaVenc and diaAtual <= 31 and diaVenc <= 31:
            print("Não está atrasada")

        else:
            print("Vence neste dia")