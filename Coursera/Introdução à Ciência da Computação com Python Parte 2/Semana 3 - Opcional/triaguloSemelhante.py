lista1 = []
class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, lista2):
        lista1 = [self.a, self.b, self.c]
        lista1.sort()

        lista2 = [lista2.a, lista2.b, lista2.c]
        lista2.sort()


        if (lista1[0]%lista2[0] == 0 and lista1[1]%lista2[1] == 0 and lista1[2]%lista2[2] == 0) or \
                (lista2[0]%lista1[0] == 0 and lista2[1]%lista1[1] == 0 and lista2[2]%lista1[2] == 0):
            return True
        else:
            return False
