import math
def elevar(
    n1:float,
    n2:float
) -> float:
    """
    Función que eleva un número al otro

    ----Argumentos----:
        n1 (float): base
        n2 (float): exponente

    ----Return----:
        float: retorna el resultado de la potenciación
    """
    result = math.pow(n1,n2)
    return result