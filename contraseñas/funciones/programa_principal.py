import os
from numeros import dígitos
from letras_minusculas import minusculas
from letras_mayusculas import mayusculas
from numeros_letras_minusculas import numeros_minusculas
from numeros_letras_mayusculas import numeros_mayusculas
from imprimir import imprimir_valores
menu = """
\t\t\t\t\t\t\t\t\tBienvenidos a tu generador de contraseñas 4000
\t\t\t\tTenemos las siguientes opciones disponibles:
\t\t\t\t\t[1] Dígitos
\t\t\t\t\t[2] Letras Minúsculas
\t\t\t\t\t[3] Letras Mayúsculas
\t\t\t\t\t[4] Dígitos y Letras Minúsculas
\t\t\t\t\t[5] Dígitos y Letras Mayúsculas
\t\t\t\t\t[10] Salir del Programa
"""
while True:
    try:
        print(menu)
        opcion = int(input('Introduce el número de acuerdo a la opción que quieres escoger: '))
        match opcion:
            case 1:
                digitos_1 = int(input('De cuantos caracteres quieres que sea tu contraseña: '))
                result = dígitos(digitos_1)
                imprimir_valores(result)
            case 2:
                digitos_2 = int(input('De cuantos caracteres quieres que sea tu contraseña: '))
                result = minusculas(digitos_2)
                imprimir_valores(result)
            case 3:
                digitos_3 = int(input('De cuantos caracteres quieres que sea tu contraseña: '))
                result = mayusculas(digitos_3)
                imprimir_valores(result)
            case 4:
                digitos_4 = int(input('De cuantos caracteres quieres que sea tu contraseña: '))
                result = numeros_minusculas(digitos_4)  
                imprimir_valores(result)
            case 5:
                digitos_5 = int(input('De cuantos caracteres quieres que sea tu contraseña: '))
                result = numeros_mayusculas(digitos_4)
                imprimir_valores(result)
            case 10:
                break
        input('\nPresiona enter para repetir el programa')
        os.system('cls')
    except ValueError:
        input('\n\nIntroduciste un valor no válido\nPresiona enter para repetirlo')
        os.system('cls')
print('\nGracias por utilizar nuestro generador de contraseñas\nTe esperamos en la proxima')
