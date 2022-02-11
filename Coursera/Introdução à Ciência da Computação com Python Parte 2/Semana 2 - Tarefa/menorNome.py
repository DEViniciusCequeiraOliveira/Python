def menor_nome(listaNomes):
    for num,nome in enumerate(listaNomes):
        nome = nome.strip().capitalize()

        if num == 0:
            nomeAtual = nome

        elif len(nome) < len(nomeAtual):
            nomeAtual = nome
    return nomeAtual

