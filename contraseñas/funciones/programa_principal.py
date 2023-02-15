import os
from numeros import dígitos
from letras_minusculas import minusculas
from letras_mayusculas import mayusculas
menu = """
\t\t\t\t\t\t\t\t\tBienvenidos a tu generador de contraseñas 4000
\t\t\t\tTenemos las siguientes opciones disponibles:
\t\t\t\t\t[1] dígitos
\t\t\t\t\t[2] Letras Minúsculas
\t\t\t\t\t[3] Letras Mayúsculas
\t\t\t\t\t[5] Salir del Programa
"""
while True:
    try:
        print(menu)
        opcion = int(input('Introduce el número de acuerdo a la opción que quieres escoger: '))
        match opcion:
            case 1:
                digitos_1 = int(input('De cuantos caracteres quieres que sea tu contraseña: '))
                result = dígitos(digitos_1) 
                print(f'\nTu contraseña es {result}')  
                print(f'Los caracteres son {list(result)}')   
            case 2:
                digitos_2 = int(input('De cuantos caracteres quieres que sea tu contraseña: '))
                result = minusculas(digitos_2)
                print(f'\nTu contraseña es {result}')
                print(f'Los caracteres son {list(result)}')   
            case 3:
                digitos_3 = int(input('De cuantos caracteres quieres que sea tu contraseña: '))
                result = mayusculas(digitos_3) 
                print(f'\nTu contraseña es {result}') 
                print(f'Los caracteres son {list(result)}')    
            case 5:
                break
        input('\nPresiona enter para repetir el programa')
        os.system('cls')
    except ValueError:
        input('\n\nIntroduciste un valor no válido\nPresiona enter para repetirlo')
        os.system('cls')
