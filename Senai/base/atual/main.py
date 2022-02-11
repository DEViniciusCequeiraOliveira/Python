import base

def chamadaPrincipal():      #Função para saber o número e a base dele
  numero = input("Digite o numero a ser convertido: ").upper()
  bas = input("\033[95m"""" --> Informe a base
  < 1 >- Hexadecimal
  < 2 >- Octal
  < 3 >- Binária
  < 4 >- Decimal\n
  ----> :""")
  return numero, bas #Retorna os valores digitado no input "numero" e "bas"

def proximaBase(): #Função que pergunta qual vai ser a próxima base
  baseF = input("\033[91m""""Escolha a base para convesão:
  { 1 }- Hexadecimal
  { 2 }- Octal
  { 3 }- Binária
  { 4 }- Decimal\n 
  ----> :""")
  return baseF #Retorna o valor da proxima base


chamada = chamadaPrincipal() #Armazena a primeira função "chamadaPrincipal()" em uma variavel com nome "chamada".

# Como return de uma função com duas variaveis sempre retorna uma lista,
#então a gente armazena cada valor em uma variavel
#desse jeito

numero = chamada[0] #A variavel "chamada" que foi criada na linha 24 que armazena os retuns da função "chamadaPrincipal()",
bas = chamada[1]    #primeiro pega a posição que ele esta no return (posição 0) e armazena em uma variavel
                    #(variavel criada com nome "número") desse jeito da linha 30


baseBool = True #foi criado essa variavel para usar no while, com o intuito de quando a pessoa escolher uma opção invalida

while baseBool:
  if bas == "1":                #Os "If" e "Elif" são para armazenar o valor da base digitada no input
    bas = 16                    #Na opção 1 do input tem "Hexadecimal" que corresponde a 16
    baseBool = False            #Essa variavel (a mesma variavel que esta sendo usada pelo while) ela vai receber "False" para poder sair do while
    proxBase = proximaBase()    #Nessa linha é pego o valor que retona na função "proximaBase()"(Ta na linha 13) e armazena na variavel "proxBase"
  elif bas == "2":              #A mesma coisa acontece nos proximos ELIF
    bas = 8
    baseBool = False
    proxBase = proximaBase()
  elif bas == "3":
    bas = 2
    baseBool = False
    proxBase = proximaBase()
  elif bas == "4":
    bas = 10
    baseBool = False
    proxBase = proximaBase()
  else:                                                 #Esse Else é para se a pessoa não digitou um número válido
    print("\033[91m""\nBase não existe!!!\n")         #A mensagem que colocou uma base errada
    chamada = chamadaPrincipal()          #Como não teve uma opção valida chama a função com input de "Qual o número" e "qual a base"
    numero = chamada[0]                   #Essa parte já foi feita lá em cima (linha 23~30)
    bas = chamada[1]                      #é necessário fazer ela denovo para armazenar o valor dentro do while,
                                          #pois não consegue repetir as atribuições que acontece na linha 29 e 30

proxBaseBool = True   #essa parte é igual da linha 34

bas = str(bas) #converter a variavel "bas" para string

while proxBaseBool:
  if proxBase == bas:       #Nessa linha é simplificado uma conta pois se a "base" que o número esta for igual a "base futura" não precisa fazer conta pois vai ser igual
    print("\033[92m"f"O valor de {numero}({bas}) na base {proxBase} é: {numero}") #é basicamente parecido com querer tranformar 20 litros para litros. A resposta vai ser 20 litros
    proxBaseBool = False    #Mesma coisa da linha 39
  elif proxBase == "1": #Mesma coisa da linha 37
    proxBase = 16
    proxBaseBool = False
  elif proxBase == "2":
    proxBase = 8
    proxBaseBool = False
  elif proxBase == "3":
    proxBase = 2
    proxBaseBool = False
  elif proxBase == "4":
    proxBase = 10
    proxBaseBool = False
  else:                       #Mesma coisa da linha 53, porém como a função "proxima base()" so retorna uma váriavel, não precisa aramzena em mais de uma variavel
    print("\033[91m""\nBase não existe!!!\n")
    proxBase = proximaBase()



if proxBase != bas: # aqui seria o IF para dar a resposta dos outros casos que não tem "base atual" e a "base futura" igual
    baseDecimal = base.decimal(numero, bas) #aqui ta chamando a primeira função do arquivo "base.py" ele pega número que esta em qualquer base e lava para decimal(A base natural que usamos no dia-dia para conversar)
    baseOutra = base.outra(baseDecimal, proxBase) #aqui pega a segunda função do arquivo "base.py" ele pega número na deciaml e leva para qualquer base
    print("\033[92m"f"O valor de {numero}({bas}) na base {proxBase} é: {baseOutra}")
