class CuentaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, cantidad):
        self.saldo += cantidad
    
    def retirar(self, cantidad):
        if cantidad <= self.saldo:  
            self.saldo -= cantidad  
        else:
            print("No hay fondos suficientes para este retiro")
    
    def mostrar_saldo(self):
        return self.saldo
    
cuenta = CuentaBancaria("Karina Mejía")

cuenta.depositar(15000)
print(f"Saldo actual: {cuenta.mostrar_saldo()}")  

cuenta.retirar(2500)
print(f"Saldo actual: {cuenta.mostrar_saldo()}")  

cuenta.retirar(13000)  
print(f"Saldo actual: {cuenta.mostrar_saldo()}")