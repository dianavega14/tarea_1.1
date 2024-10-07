def es_primo(num):
    if num == 0 or num == 1:
        print(num, "no es un número primo")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "no es un número primo")
                break 
        else:
            print(num, "es un número primo")
    else:
        print(num, "no es un número primo")

numero = int(input("Ingrese un número: "))
es_primo(numero)  