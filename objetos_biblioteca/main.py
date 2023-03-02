from objetos import Persona
from objetos import menu
menu()
opcion = int(input("Introduce la opción: "))
match opcion:
    case 1:
        nombre = str(input("Introduce el nombre del Usuario: "))
        libro_prestado = str(input(f"Introduce el nombre el libro prestado por el Usuario {nombre}"))
        nombre = Persona(nombre,libro_prestado)
        
        