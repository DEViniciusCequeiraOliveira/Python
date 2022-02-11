class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        if self.a > self.b and self.a > self.c:
            return self.b ** 2 + self.c ** 2 == self.a ** 2

        elif self.b > self.a and self.b > self.c:
            return self.a ** 2 + self.c ** 2 == self.b ** 2

        elif self.c > self.a and self.c > self.b:
            return self.a ** 2 + self.b ** 2 == self.c ** 2
