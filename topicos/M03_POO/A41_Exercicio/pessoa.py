import contas

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None  = None

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = Cliente('Aecio', 25)
    c1.conta = contas.ContaCorrente(111,222,333,150)
    print(c1.__dict__)
    print(c1.conta.__dict__)