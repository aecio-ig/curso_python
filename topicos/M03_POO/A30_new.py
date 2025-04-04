class A:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, x):
        print('Iniciando objeto')

    def __repr__(self):
        return self.__class__.__name__
    

a = A('a')
a