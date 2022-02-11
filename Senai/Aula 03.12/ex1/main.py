# Escreva um programa que leia 20 números de um arquivo texto (que você deve criar) chamado 'números.txt'
# e separe-os em outros dois arquivos: 'par.txt' que conterá os números pares do arquivo 'números.txt' e
# 'impar.txt' que conterá os números ímpares do arquivo 'números.txt'.

with open("numero.txt", "r") as num:
    numeros = num.readlines()

with open("par.txt", "w") as pares:
    for n in numeros:
        n = int(n)
        if n % 2 == 0:
            pares.writelines(f"{n}\n")

with open("impar.txt", "w") as impares:
    for n in numeros:
        n = int(n)
        if n % 2 != 0:
            impares.write(f"{n}\n")

