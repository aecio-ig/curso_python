## decoradores servem para Adicionar / Remover / Restingir / Aterar

def is_string(string):
    if not isinstance(string, str):
        raise TypeError('Tipo errado migão, tem que ser str')


def decorator(func):
    def returned(*args, **kwargs):
        for arg in args:
            is_string(arg)
        return func(*args, **kwargs)
    return returned

@decorator
def invert_str(string):
    return string[::-1]

invertida = invert_str('Aecio')

print(invertida)