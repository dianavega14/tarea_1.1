class Calculadora:
    def sumar(self, a, b):
        return a + b
    def restar(self, a, b):
        return a - b
    def multiplicar(self, a, b):
        return a * b
    def dividir(self, a, b):
        if b == 0:
            return "No se puede dividir por cero."
        else: 
            return a / b

calculadora = Calculadora()
n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))

suma = calculadora.sumar(n1, n2)
resta = calculadora.restar(n1, n2)
multiplicacion = calculadora.multiplicar(n1, n2)
division = calculadora.dividir(n1, n2)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")