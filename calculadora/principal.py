import os
from sumar import sumar
from restar import restar
from multiplicar import multiplicar
from dividir import dividir
from potenciacion import elevar
from radicacion import raiz_cuadrada
menu = """
\t\t\t\t\t\t\t\tBienvenidos a la calculadora
\t\t\t\tTenemos las siguientes operaciones disponibles:
\t\t\t\t\t[1] Sumar
\t\t\t\t\t[2] Restar
\t\t\t\t\t[3] Multiplicación
\t\t\t\t\t[4] División 
\t\t\t\t\t[5] Potenciación
\t\t\t\t\t[6] Radicación
\t\t\t\t\t[10] Salir del Programa
"""
while True:
    try:
        os.system('cls')
        print(menu)
        opcion = int(input('Introduce el número correspondiente a la opción deseada: '))
        match opcion:
            case 1:
                num_1 = float(input('Introduce un número: '))
                num_2 = float(input('Introduce otro número: '))
                resultado = sumar(num_1,num_2)
                print(f'El resultado de la suma es {resultado}')
            case 2:
                num_1 = float(input('Introduce un número: '))
                num_2 = float(input('Introduce otro número: '))
                resultado = restar(num_1,num_2)
                print(f'El resultado de la suma es {resultado}')
            case 3:
                num_1 = float(input('Introduce un número: '))
                num_2 = float(input('Introduce otro número: '))
                resultado = multiplicar(num_1,num_2)
                print(f'El resultado de la multipliación es {resultado}')
            case 4:
                num_1 = float(input('Introduce un número: '))
                num_2 = float(input('Introduce otro número: '))
                resultado = dividir(num_1,num_2)
                print(f'El resultado de la division es {resultado}')
            case 5:
                num_1 = float(input('Introduce un número: '))
                num_2 = float(input('Introduce otro número: '))
                resultado = elevar(num_1,num_2)
                print(f'El resultado de la potenciación es {resultado}')
            case 6:
                num_1 = float(input('Introduce un número: '))
                num_2 = float(input('Introduce otro número: '))
                resultado = raiz_cuadrada(num_1,num_2)
                print(f'El resultado de la radicación es es {resultado}')
            case 10:
                break
        input('Final del programa\nPresiona Enter para reiniciar el programa ')
    except ValueError:
        input('Introduciste un válor no válido\nPresiona enter para reintentarlo')
    except ZeroDivisionError:
        input('Dividir entre 0 es imposible\nPresione enter para reintentarlo')