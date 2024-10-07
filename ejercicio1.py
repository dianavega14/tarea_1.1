class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base + self.altura) * 2

r1 = Rectangulo(5, 3)

print(f"Área: {r1.area()}")
print(f"Perímetro: {r1.perimetro()}")