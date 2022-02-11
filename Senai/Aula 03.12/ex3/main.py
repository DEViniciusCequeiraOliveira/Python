with open("vetor1.txt", "r") as leitor1:
    vet1 = leitor1.readlines()

with open("vetor2.txt", "r") as leitor2:
    vet2 = leitor2.readlines()

with open("soma.txt", "w") as somar:
    for i in range(len(vet1)):
        soma = int(vet1[i]) + int(vet2[i])
        somar.write(f"{soma}\n")