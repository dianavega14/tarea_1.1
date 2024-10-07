import string
import random

length = int(input("Ingrese la longitud de la contraseña (mínimo 8 caracteres): "))

if length < 8:
    print("La longitud mínima de la contraseña es 8 caracteres.")
else:
    letras_mayusculas = string.ascii_uppercase  
    letras_minusculas = string.ascii_lowercase  
    digitos = string.digits  
    simbolos = string.punctuation  
    
    todos_los_caracteres = letras_mayusculas + letras_minusculas + digitos + simbolos

    contrasena = ''.join(random.choice(todos_los_caracteres) for _ in range(length))

    print("La contraseña aleatoria es: " + contrasena)
