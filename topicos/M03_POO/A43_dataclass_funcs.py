from dataclasses import dataclass, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    p1 = Pessoa('Aecio','Lucio')
    print(asdict(p1).keys())
    print(astuple(p1)[0])
    print(asdict(p1).values())
