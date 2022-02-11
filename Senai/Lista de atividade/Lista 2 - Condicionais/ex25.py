# 25. O Peso normal de uma criança pode ser calculado através da fórmula:
# 𝑃𝑒𝑠𝑜𝑁𝑜𝑟𝑚𝑎𝑙 = (𝐼𝑑𝑎𝑑𝑒 − 6) / 4,4 + 2,3(𝐼𝑑𝑎𝑑𝑒 − 6) + 22
# Escreva um programa em Python que leia a idade e o peso de uma criança e, se for o
# caso, imprima uma dessas mensagens de acordo com a quantidade de quilos acima do
# peso com que a criança esteja:
# Quantidade de quilos acima do
# peso
# Mensagem
# De 2 a 5 “Parar de tomar refrigerante.”
# Acima de 5 até 10 “Parar de comer doces.”
# Acima de 10 “Parar de tomar refrigerante e de
# comer doces.”

idade = int(input("Digite a idade da criança: "))
peso = int(input("Digite o peso da criança em Kg: "))

pesoNormal = (idade - 6) / (4.4) - 2.3 * (idade - 6) + 22

pesoAcima = peso - pesoNormal

if pesoAcima >= 2 and pesoAcima <= 5:
    print("Parar de tomar refrigerante.")

elif pesoAcima > 5 and pesoAcima <= 10:
    print("Parar de comer doces.")

elif pesoAcima > 10:
    print("Parar de tomar refrigerante e de comer doces.")

else:
    print("Parabéns, você esta bem!!!")