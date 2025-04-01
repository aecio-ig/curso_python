"""
Modulo de docstring

Aqui temos exemplos de uso de docstrings
"""

def soma(x: int | float, y: int| float) -> int|float:
    """
    Soma x e y

    Este módulo soma 

    :return: a soma entre x e y
    :raises: TypeError: Levanta o Ero se o tipo n tiver definido
    :raises: NotImplementedError: Dá erro se n implementado o metodo obrigatorio
    """
    return x+y

soma(1,2)