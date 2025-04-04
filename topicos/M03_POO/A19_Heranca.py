# class Foo(object):
#     ... 

# help(Foo)


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def falar_nome_classe(self):
        print(self.__class__.__name__)

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...

c1 = Cliente('Aecio', 35)
c1.falar_nome_classe()
a1 = Aluno('Laura', 20)
a1.falar_nome_classe()

help(c1)