from random import choice
def dígitos(cantidad):
    """_summary_

    Returns:
        _type_: _description_
    """
    caracteres = ['1','2','3','4','5','6','7','8','9','0']
    acomulador = ''
    for i in range(cantidad):
        acom = choice(caracteres)
        str(acom)
        acomulador = acomulador + acom
    return acomulador