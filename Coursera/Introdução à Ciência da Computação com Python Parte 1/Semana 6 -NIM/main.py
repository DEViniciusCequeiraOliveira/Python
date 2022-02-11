def jogo():
    print("Bem-vindo ao jogo do NIM! Escolha: \n")
    opcao = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato"))

    while opcao !=1 and opcao !=2:
        opcao = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato"))

    if opcao == 1:
        print("Voce escolheu uma partida isolada!")
        partida()

    elif opcao == 2:
        print("Voce escolheu um campeonato!")
        campeonato()

def campeonato():
    print("\n**** Rodada 1 ****\n")
    partida()
    print("\n**** Rodada 2 ****\n")
    partida()
    print("\n**** Rodada 3 ****\n")
    partida()

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    vezDoPC = False

    if n % (m + 1) == 0:
        print('\nVoce começa!\n')

    else:
        print('\nComputador começa!\n')
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:

                print('\nO computador tirou uma peça')
            else:
                print('\nO computador tirou', computadorRemove, 'peças')

            vezDoPC = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print('\nVocê tirou uma peça')
            else:
                print('\nVocê tirou', jogadorRemove, 'peças')
            vezDoPC = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.\n')
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.\n')

    print('Fim do jogo! O computador ganhou!')

def usuario_escolhe_jogada(n,m):
    jogadaValida = False

    while not jogadaValida:
        jogadorRemove = int(input('Quantas peças você vai tirar? '))
        if jogadorRemove > m or jogadorRemove < 1:
            print('\nOops! Jogada inválida! Tente de novo.\n')

        else:
            jogadaValida = True

    return jogadorRemove

def computador_escolhe_jogada(n,m):
    computadorRemove = 1

    while computadorRemove !=m:
        if (n - computadorRemove) % (m+1) ==0:
            return computadorRemove

        else:
            computadorRemove +=1

    return computadorRemove


jogo()