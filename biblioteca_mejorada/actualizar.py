def actualizar_usuario(
    dicc:dict
) -> dict:
    nombre:str = str(input('\nIngresa el nombre del usuario que va a prestar el nuevo libro: '))
    libro:str = str(input(f'Ingresa el nuevo libro que presto el usuario {nombre}: '))
    date:str = str(input(f'Ingresa la fecha donde el usuario {nombre} presto el libro {libro}:  '))
    dia,mes,año = date.split('/')
    nombre = nombre.title()
    diccionario_interno= {
        "libro":libro,
        "fecha": {
                "dia": dia,
                "Mes":mes,
                "Año":año
            }
    }
    dicc[nombre].append(diccionario_interno)
    return dicc