def imprime_matriz(matriz):
    linhaLista = []
    for linha in matriz:
        for coluna in linha:
            linhaLista.append(str(coluna))

        print(" ".join(linhaLista))
        linhaLista = []
