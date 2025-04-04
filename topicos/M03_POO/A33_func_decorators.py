from contextlib import contextmanager

def meu_repr(self):
    class_name = self.__class__.__name__  # Nome da classe
    class_dict = self.__dict__  # Atributos da instância
    return f'{class_name}({class_dict})'

def adiciona_repr(cls):
    cls.__repr__ = meu_repr  # Adiciona um __repr__ customizado na classe
    return cls

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)  # Chama o método original
        if 'Terra' in resultado:
            return 'Você está em casa'  # Modifica a saída para "Terra"
        return resultado
    return interno

def log_metodo(metodo):
    def wrapper(self, *args, **kwargs):
        print(f'Chamando {metodo.__name__} com args={args}, kwargs={kwargs}')
        resultado = metodo(self, *args, **kwargs)
        print(f'Resultado de {metodo.__name__}: {resultado}')
        return resultado
    return wrapper

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta  # Modifica o comportamento do método
    @log_metodo   # Faz log antes e depois de chamar o método
    def falar_nome(self):
        return f'O planeta é {self.nome}'

# Testando as classes e decorators
brasil = Time('Brasil')
portugal = Time('Portugal')
print(brasil)
print(portugal)

terra = Planeta('Terra')
marte = Planeta('Marte')
print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())