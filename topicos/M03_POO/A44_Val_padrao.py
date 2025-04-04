from dataclasses import dataclass, field


@dataclass
class Pessoa:
    nome: str = 'Missing'
    sobrenome: str = 'Not sent'
    idade: int = 30
    enderecos: list[str] = field(default_factory=list) ## fild serve para configurar campos na dataclass 
    ## pode ser usado para configurações mas dados mutaveis deve ser configurado da forma acima para que n seja atribuido para todos.
    