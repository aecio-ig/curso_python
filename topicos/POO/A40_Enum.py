# membro = Classe(valor), Classe['chave']
 # chave = Classe.chave.name
 # valor = Classe.chave.value


import enum


Direcoes = enum.Enum('Direcao', ['ESQUERDA', 'DIREITA', 'CIMA', 'BAIXO'])

class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Não é uma direcao')
    print(f'Movendo na direção {direcao.value}')


print(Direcoes.ESQUERDA.name)
print(Direcoes.ESQUERDA.value)
    
