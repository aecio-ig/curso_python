# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint

lista = [numero + 5  for numero in range(30)]
print(lista)


## mapeamento de dados em list pombprehention
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    produto 
    for produto in produtos
]

print(novos_produtos)
print(*novos_produtos, sep='\n')



novos_produtos = [
    # multiplica o valor da variavel se o produtos[preço] do laço for maior que 20
    {**produto, 'preco': produto['preco']* 1.05 } 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]
print()
print(novos_produtos)
print()
pprint.pprint(novos_produtos)


#### filtro em list comprehension
lista = [n for n in range(10) if n < 5]
pprint.pprint(lista)