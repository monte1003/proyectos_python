from random import choice
def numeros_minusculas(cantidad:int) -> str:
    """
    Función que se encarga de generar un string con letras minúsculas y números al azar (0 - 9)
    
    ----Argumentos----:
    
        cantidad (int): La cantidad de caracteres que queramos que tenga el string

    ----Return----:
    
        str : Devuelve el string con los caracteres pasados como argumentos de la función
    """
    caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','x','y','z']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    new_list = caracteres + numeros
    acomulador = ''
    for i in range(cantidad):
        acom = choice(new_list)
        str(acom)
        acomulador = acomulador + acom
    return acomulador
