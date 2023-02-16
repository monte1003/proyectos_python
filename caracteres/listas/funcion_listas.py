def palabra(
    p: str
) -> list:
    """
    Programa que transforma una frase en una lista con cada una de las palabras de esa frase

    ----Argumentos----:
    
        p (str): Frase que transformaremos a lista

    ----Return----:
    
        list: La frase transformada a lista
    """
    p = p.split(" ")
    caracteres = []
    for i in p:
        caracteres.append(i)
    return caracteres
