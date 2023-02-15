from random import choice
def numeros_mayusculas(cantidad:int) -> str:
    """
    Función que se encarga de generar un string con letras mayúsculas y números al azar (0 - 9)

    ----Argumentos----:
    
        cantidad (int): La cantidad de caracteres que queramos que tenga el string

    ----Return----:
    
        str : Devuelve el string con los caracteres pasados como argumentos de la función
    """
    caracteres = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','X','Y','Z']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    new_list = caracteres + numeros
    acomulador = ''
    for i in range(cantidad):
        acom = choice(new_list)
        str(acom)
        acomulador = acomulador + acom
    return acomulador