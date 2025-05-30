# Classes decoradoras 
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador
        print('Init')

    def __call__(self, func):
        def interna (*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna

@Multiplicar(10)
def soma(x,y):
    return x + y

soma(1,2)