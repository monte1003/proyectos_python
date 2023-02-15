from random import choice
def minusculas(cantidad:int) -> str:
    """
    Función que genera un string con letras minúsculas al azar 
    
    ----Argumentos----:
    
        cantidad (int): La cantidad de caracteres que queramos que tenga el string

    ----Return----:
    
        str : Devuelve el string con los caracteres pasados como argumentos de la función
    """
    caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','x','y','z']
    acomulador = ''
    for i in range(cantidad):
        acom = choice(caracteres)
        str(acom)
        acomulador = acomulador + acom
    return acomulador