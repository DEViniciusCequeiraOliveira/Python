largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

larguraOriginal = largura

while altura > 0:
    altura -= 1
    while largura > 0:
        print("#", end="")
        largura -= 1
    if altura > 0 and largura == 0:
        print("")
    largura = larguraOriginal

