
# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)


class Meta(type): ## util para fazer algo antes de gerar a classe
    def __new__(mcs, name, bases, dct):
        print('Metaclass new')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 123  ##### espalha o atributo para ttodos que o herdam e não alteram ou usam a keyword
        print(cls.__dict__)

        ## aqui tambem podemos verificar se metodo foi adicionado a classe qe tá chamando essa classe como meta
        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('Não implementado o metodo na classe')

        return cls


class Pessoa(object, metaclass=Meta):
    def __new__(cls, *args,**kwargs):
        print('Meu NEW')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
        print("Meu init")
        self.nome = nome
    
    def falar(falancia):
        print(f'Falando : {falancia}')

p = Pessoa('Tião')
print(Pessoa.attr)