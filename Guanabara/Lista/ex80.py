valores = []

for c in range(0,5):
    valor = int(input("Digite um valor: "))

    if c == 0 or valor > valores[-1]:
        valores.append(valor)
        print("Adicionou na última posição")

    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos,valor)
                print(f"Adicionou na posição {pos}ª")
                break
            pos+=1
print(valores)