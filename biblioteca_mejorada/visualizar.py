import time

def visualizar_usuarios(
    dicc :dict
) -> dict:
    """
        Función que consiste en visualizar los usuarios en un diccionario

    ----Argumentos----:
        
        persona (str):El nombre de la persona (la key en mi diccionario)
        dicco (dict): nombre de nuestro diccionario

    ----Retorno----:
        
        dict: Devuelve el nombre de la persona y el valor accediendo a su valor por medio de la clave "persona" en nuestro diccionario
    """
    persona = str(input('\nIntroduce el nombre del usuario el cual deseas ver su información: '))
    persona = persona.title()
    print(f'Libros Prestados del usuario {persona}')
    for i in dicc[persona]:
        for key,value in i.items():
            print(f'\n{key}: {value}')
            time.sleep(0.5)