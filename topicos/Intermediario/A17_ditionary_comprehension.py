produto = {
    'nome' : 'Caneta',
    'preco' : 2.4,
    'categoria': 'Escritorio'
}

for chave, valor in produto.items():
    print(chave, valor)


dc = {
    chave: valor.upper() if type(valor) in [int, str] else valor ## faz u ternario pra verificar se pode alterar
    for chave, valor in produto.items()
}

print(dc)


s1 = {i for i in range(10)}
print(s1)

