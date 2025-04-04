
# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html@@ -0,0 +1,20 @@
# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'
        print(self.nome_completo)

if __name__ == '__main__':
    p1 = Pessoa('Aecio', 'Lucio', 25)
    print(p1)


## podemos congelar a dataclass 
@dataclass(frozen=True)
class Aba:
    nome: str
    sobrenome: str
    idade: int

if __name__ == '__main__':
    p1 = Aba('Aecio', 'Lucio', 25)
    print(p1)