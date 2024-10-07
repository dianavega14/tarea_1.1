def fibonacci():
    n = int(input("Ingrese el número de términos: "))

    if n <= 0:
        print("Ingrese otro número")
        return

    a, b = 0, 1
    print("Secuencia de Fibonacci:")
    
    for i in range(n):
        print(a, end=", " if i < n-1 else "")
        a, b = b, a + b
    
    print()  
    
fibonacci()