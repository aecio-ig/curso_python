# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html

class MyList:
    def __init__(self) -> None:
        self._data: dict[int, str | int | float] = {}

    def append(self, value:str|int|float):
        self._data[len(self._data)] = value


if __name__ == '__main__':
    lista = MyList()

    lista.append('aecio')
    lista.append(150)
    lista.append('Alous')
    
    print(lista.__dict__)