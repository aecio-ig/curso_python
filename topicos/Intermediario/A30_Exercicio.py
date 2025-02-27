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

# Gere novos_produtos por deep copy (cópia profunda)
import copy
copiaprofunda_la_ele =  copy.deepcopy(produtos)
for i in range(15):
    copiaprofunda_la_ele.append({'nome':f'prd{i}', 'preco':f'preco{i*3/i if i > 0 else 2}'})
copiaprofunda_la_ele.sort()
print(copiaprofunda_la_ele)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)



# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

print(copiaprofunda_la_ele.sort())
