def eliminar_usuario(
    dicc:dict
) -> dict:
    """_summary_

    Args:
        persona (str): _description_
        dicc (dict): _description_

    Returns:
        dict: _description_
    """
    persona = str(input('\nIngresa el nombre del usuario que deseas eliminar: '))
    persona = persona.title()
    dicc.pop(persona)
    return dicc