import random

def adivina_numero():
    numero_aleatorio = random.randint(1, 100) 
    intento = None
    intentos = 0
    
    print("¡Adivina el número entre 1 y 100!")
    
    while intento != numero_aleatorio:
        intento = int(input("Ingresa tu intento: "))
        intentos += 1
        
        if intento < numero_aleatorio:
            print("El número es mayor.")
        elif intento > numero_aleatorio:
            print("El número es menor.")
    
    print(f"¡Felicitaciones! Has adivinado el número en {intentos} intentos.")

adivina_numero()
