numero = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
          'onze','doze','treze','quartoze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')

x = int(input("Digite um número treze entre 0 e 20: "))

while not 0 <= x <= 20:
    x = int(input("Tente novamente. Digite um número treze entre 0 e 20: "))

print(f"VocÊ digitou o número {numero[x]}")

