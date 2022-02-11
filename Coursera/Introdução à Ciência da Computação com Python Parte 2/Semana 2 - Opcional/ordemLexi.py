def primeiro_lex(lista):
    for pos,name in enumerate(lista):
        if pos == 0:
            nameAtual = name

        elif name < nameAtual:
            nameAtual = name

    return nameAtual
