primeiroTermo = int(input("Qual o primeiro termo da PA? "))
razao = int(input("Qual a razão da PA? "))
ultimoTermo = razao * 10 + primeiroTermo

print("_" * 12, "\n\nA sua PA é:")

for num in range (primeiroTermo,ultimoTermo,razao):
    print(num)