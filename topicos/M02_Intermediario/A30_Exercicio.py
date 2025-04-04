# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


aumentado_10 = [{'nome': x['nome'], 'preco':((x['preco']*10) / 100)+ x['preco']} for x in produtos ]
print('Precos aumentado 10%')
print(aumentado_10)
print()

# Gere novos_produtos por deep copy (cópia profunda)
import copy
print('Deep copy')
copiaprofunda_la_ele =  copy.deepcopy(produtos)
print(copiaprofunda_la_ele)
print()

# Ordene os produtos por nome decrescente (do maior para menor)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key= lambda p: p['nome']
)
print('Ordenadoos por nome')
print(produtos_ordenados_por_nome)
print()


produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key= lambda p: p['preco']
)
print('Ordenados por preco')
print(produtos_ordenados_por_preco)

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)



# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

