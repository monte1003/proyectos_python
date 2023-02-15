from random import choice
def minusculas(cantidad):
    """_summary_

    Args:
        cantidad (_type_): _description_

    Returns:
        _type_: _description_
    """
    caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','x','y','z']
    acomulador = ''
    for i in range(cantidad):
        acom = choice(caracteres)
        str(acom)
        acomulador = acomulador + acom
    return acomulador