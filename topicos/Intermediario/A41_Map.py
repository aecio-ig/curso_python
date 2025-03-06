from functools import partial
from types import GeneratorType


# map - para mapear dados palica uma função em cada item da lista
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


novos_produtos = [{**p, 'preco':123} for p in produtos]

def alterar_preco(produto):
    return {**produto, 'preco':321}

novos_produtos = map(alterar_preco, produtos)


print_iter(novos_produtos)