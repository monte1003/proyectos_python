from random import choice
def mayusculas(cantidad:int) -> str:
    """
    Función que genera un string con letras mayúsculas al azar 
    
    ----Argumentos----:
    
        cantidad (int): La cantidad de caracteres que queramos que tenga el string

    ----Return----:
    
        str : Devuelve el string con los caracteres pasados como argumentos de la función
    """
    caracteres = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','X','Y','Z']
    acomulador = ''
    for i in range(cantidad):
        acom = choice(caracteres)
        str(acom)
        acomulador = acomulador + acom
    return acomulador
