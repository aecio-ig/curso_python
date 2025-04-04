a, b = 1, 2
a, b = b, a 

print(a)
print(b)


pessoa = {
    'nome': 'Girombeta',
    'sobrenome': 'Astronautica'
}


a,b = pessoa.values()
print(a, b)


# cchave e valor 
(a1, a2), (b1, b2) = pessoa.items()

print (a1,a2)
print(b1,b2)


for chave, valor in pessoa.items():
    print(chave, valor)



print('------------------')

dados_pessoa = {
    'idade': 78,
    'altura': 7.56
}
pessoa = {
    'nome': 'Girombeta',
    'sobrenome': 'Astronautica'
}
pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)



## kwargs
## saõ KEY WORDS -- Args
def mostro_argumentos_nomeados(*args, **kwargs):
    print(f'Esse é o Kwaergs {kwargs}')
    for chave, valor in kwargs.items():
        print(chave, valor)
    
    print()
    print()

mostro_argumentos_nomeados(**pessoa_completa) ## os dois asteristicos vira dois valores


config = {
    'con_1': 4,
    'con_2': 4,
    'con_3': 4,
    'con_4': 4,
    'con_5': 4,
}


mostro_argumentos_nomeados(**config)
