# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations
from itertools import permutations
from itertools import product

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]



## combination
print(*list(combinations(pessoas, 2)), sep='\n')

print('Permutation')
print()
## Permutation
print(*list(permutations(pessoas, 2)), sep='\n')
print()

## é a brabona que reaciona tudo a todos
print('Produto')
print(*product(*camisetas), sep='\n')

