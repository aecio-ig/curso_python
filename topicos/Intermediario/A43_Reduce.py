from functools import reduce


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

def funnc_reduce(acumulador, produto):
    print(acumulador)
    print(produto)
    print()
    return acumulador + produto['preco']

total = reduce(
    funnc_reduce,
    produtos,
    0 ### passar sempre o valor inicial
)



# reduce reduz o iteravel a um unico valor
# total = 0

# for i in produtos:
#     total += i['preco']

# print(total)


