from random import choice
def numeros_mayusculas(cantidad):
    """_summary_

    Args:
        cantidad (_type_): _description_

    Returns:
        _type_: _description_
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