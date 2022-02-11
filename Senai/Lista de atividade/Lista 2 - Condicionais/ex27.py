# 27. Um novo terminal de computador foi instalado na biblioteca para facilitar a consulta de
# livros. A você coube fazer a interface de apresentação. Como parte deste projeto escreva
# um pequeno programa em Python que leia do teclado um valor correspondente à hora do
# dia (XX h XX min XX seg) e imprima na tela “Bom Dia!”, “Boa Tarde!” ou “Boa Noite!” de
# acordo com o horário. Se o horário estiver compreendido entre 0h e 6h, deve imprimir
# “Sistema Indisponível”.

hora = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

if hora >= 6 and hora <= 11:
    if minutos >= 0 and minutos <= 59:
        if segundos >= 0 and segundos <= 59:
            print("Bom Dia!")

elif hora >= 12 and hora <= 17:
    if minutos >= 0 and minutos <= 59:
        if segundos >= 0 and segundos <= 59:
            print("Boa Tarde!")

elif hora >= 18 and hora <= 23:
    if minutos >= 0 and minutos <= 59:
        if segundos >= 0 and segundos <= 59:
            print("Boa Noite!")

elif hora >= 00 and hora <= 5:
    if minutos >= 0 and minutos <= 59:
        if segundos >= 0 and segundos <= 59:
            print("Sistema Indisponível")
