nome = input("Qual o nome? ").strip().upper()
separado = nome.split()
junto = "".join(separado)
inverso = ""

for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print("É palindromo")

else:
    print("Não é palindromo")
