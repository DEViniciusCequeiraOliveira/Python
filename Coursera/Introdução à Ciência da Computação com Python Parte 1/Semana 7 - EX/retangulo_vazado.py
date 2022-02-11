largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

larguraOriginal: int = largura
alturaOriginal = altura

while altura > 0:
    while largura > 0:
        if altura == alturaOriginal or altura == 1:
            print("#", end="")
        else:
            if larguraOriginal == largura or largura == 1:
                print("#", end="")
            else:
                print(" ", end="")
        largura-= 1

    altura -= 1
    if altura > 0:
        print("")

    largura = larguraOriginal

