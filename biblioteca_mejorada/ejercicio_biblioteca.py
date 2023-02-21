import os
from create import agregar
from eliminar import eliminar_usuario
from actualizar import actualizar_usuario
from visualizar import visualizar_usuarios
from visualizar_2 import visualizar_total
usuarios = {}   
if __name__ == '__main__':
    while True:
        menu = """
        \t\t\t\t\t\t\t\t                    Biblioteca Karl Parris.J:
        \n\t          Presiona 1 para Agregar Usuario 
        \t  Presiona 2 para Eliminar Usuario
        \t  Presiona 3 para Actualizar Libro que Presto el Usuario
        \t  Presiona 4 para Visualizar la base de datos
        \t  Presiona 5 para salir del Programa
        """
        print(menu)
        try:
            opcion:int = int(input('Ingresa una opción: '))
            os.system('cls')
            match opcion:
                case 1:
                    print('\t\t\t\t\t\t\t\tAgregar Usuario')
                    agregar(usuarios)
                    os.system('cls')
                case 2:
                    print('\t\t\t\t\t\t\t\tEliminar Usuario')
                    eliminar_usuario(usuarios)
                    os.system('cls')
                case 3:
                    print('\t\t\t\t\t\t\t\tActualizar Usuario')
                    actualizar_usuario(usuarios)
                    os.system('cls')
                case 4:
                    print('\t\t\t\t\t\t\t\tVisualizar Usuarios')
                    n = """
                    Presiona 1 para visualizar a un usuario en específico
                    Presiona 2 para visualizar toda la base de datos
                    """ 
                    print(n)
                    op = input('\n\tSelecciona una opcion: ')
                    if op == '1':
                        visualizar_usuarios(usuarios)
                    elif op == '2':
                        visualizar_total(usuarios)
                case 5:
                    print('\t\t\t\nFIN DEL PROGRAMA\t\t\t\nGracias por utilizar nuestro sistema de bases de datos\t\t\t\n\nTe esperamos en la otra\t\t\t\nSomos Bibliotecas Abiertas')
                    break
        except ValueError:
            input('Ingresaste una opción no válida\nPresiona enter para volver a intentarlo ')
            os.system('cls')
        except KeyError:
            input('El nombre del usuario no se encuentra en la base de datos\nPresiona enter para volver a intentarlo ')
            os.system('cls')
