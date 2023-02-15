def imprimir_valores(valor:str):
    """
    Funcion que se encarga de imprimir los valores que le pasemos

    ----Argumentos----:
    
        valor (str): Valor que le pasamos a la función que imprima
    
    ----Return----:
    
        Devuelve un print con 'tu contraseña es {valor}'
        Devuelve otro print con ese valor pasado a un formato 'list'
    """
    print(f'\nTu contraseña es {valor}')  
    print(f'Los caracteres son {list(valor)}')  