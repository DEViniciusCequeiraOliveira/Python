def produto():
    try:
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")

        return int(num1) * int(num2)
    except (ValueError,TypeError):
        if not num1.isdecimal() and not num2.isdecimal():
            print("Os dois digitos são inválido\n")
            return produto()

        elif not num1.isdecimal():
            print("O primeiro digito é inválido\n")
            return produto()

        elif not num2.isdecimal():
            print("O segundo digito é inválido\n")
            return produto()

print(produto())