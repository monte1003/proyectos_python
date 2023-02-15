from random import choice
def numeros_minusculas(cantidad):
    """_summary_

    Args:
        cantidad (_type_): _description_

    Returns:
        _type_: _description_
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
