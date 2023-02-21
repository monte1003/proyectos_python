def agregar(
    dicc: dict
) -> dict:
    """_summary_

    Args:
        nombre (str): _description_
        libro (str): _description_
        fecha (str): _description_
        dicc (dict): _description_

    Returns:
        dict: _description_
    """
    
    lista = []
    nombre:str = str(input('\nIngresa el nombre y apellido del usuario: '))
    nombre = nombre.title()
    dicc[nombre] = lista
    cantidad = int(input(f'Libros prestados del usuario {nombre}: '))
    for i in range(cantidad):
        e:str = str(input(f'\nNombre del libro número {i+1} prestado por el Usuario {nombre}: '))
        date:str = str(input(f'Ingresa la fecha donde el usuario {nombre} presto el libro "{e}": '))
        dia,mes,año = date.split('/')
        diccionario_interno = {
            "libro":e,
            "fecha": {
                "dia": dia,
                "Mes":mes,
                "Año":año
            }
        }
        lista.append(diccionario_interno)
    return dicc