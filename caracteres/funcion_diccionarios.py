def palabra(
    p:str
) -> dict:
    """_summary_

    Args:
        p (str): _description_

    Returns:
        dict: _description_
    """
    p = p.split(" ")
    diccionario = {}
    for pal in p:
        longitud = len(pal)
        diccionario.update({pal:{"caracteres":longitud}})
    return diccionario