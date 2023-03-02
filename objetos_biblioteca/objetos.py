import datetime
class Persona():
    def __init__(self,
                nombre:str,
                libro:str) -> None:
        self.nombre = nombre
        self.libro = libro
        self.fecha = datetime.date.today()
        self.usuarios = {
            "Usuarios":self.nombre,
            "Libro Prestado":self.libro,
            "Fecha":self.fecha
        }
        
    def imprimir(self):
        for key,value in self.usuarios.items():
            print(f"{key} => {value}")
    
    def actualizar_usuario(self,nombre):
        libro = str(input(f"Introduce el nuevo libro prestado por el usuario {nombre}: "))
        self.usuarios["Libro Prestado"] = libro
    
    def eliminar_usuario(self,nombre):
        del nombre
        

def menu():
    menu = """
    \t\t\t\t\tBienvenido a Biblioteca Karl C. Parrish Jr.
    \t\t\tTenemos las siguientes opciones disponibles:
    \t\t [1] Agregar Usuario
    \t\t [2] Eliminar Usuario
    \t\t [3] Actualizar Usuario
    \t\t [4] Visualizar Base de Datos
    """
    print(menu)
