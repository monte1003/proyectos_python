from random import choice
def mayusculas(cantidad):
    """_summary_

    Args:
        cantidad (_type_): _description_

    Returns:
        _type_: _description_
    """
    caracteres = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','X','Y','Z']
    acomulador = ''
    for i in range(cantidad):
        acom = choice(caracteres)
        str(acom)
        acomulador = acomulador + acom
    return acomulador
