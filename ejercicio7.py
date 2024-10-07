def tabla_multiplicar():
    n = int(input("Ingrese un número entero: "))
    
    print(f"Tabla de multiplicar del {n}:")
    
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

tabla_multiplicar()