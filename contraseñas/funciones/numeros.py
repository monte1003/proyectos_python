from random import choice
def dígitos(cantidad:int) -> str:
    """
    Función que se encarga de generar un string con números al azar (0 - 9)

    ----Argumentos----:
    
        cantidad (int): La cantidad de caracteres que queramos que tenga el string

    ----Return----:
    
        str : Devuelve el string con los caracteres pasados como argumentos de la función
    """
    caracteres = ['1','2','3','4','5','6','7','8','9','0']
    acomulador = ''
    for i in range(cantidad):
        acom = choice(caracteres)
        str(acom)
        acomulador = acomulador + acom
    return acomulador