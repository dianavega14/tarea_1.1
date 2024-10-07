def contador_vocales():
    frase = input("Ingrese una frase: ")
    vocales = "aeiouAEIOU"
    contador = 0
    
    for letra in frase:
        if letra in vocales:
            contador += 1
    
    print(f"El número total de vocales es: {contador}")

contador_vocales()