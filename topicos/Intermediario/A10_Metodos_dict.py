# Métodos úteis dos dicionários em Python
pessoa = {
    'nome': 'Aecio',
    'idade': 15,
    'trabalho': 'fazedor de programas'
}

for chave in pessoa:
    print(chave, pessoa[chave])

# len - quantas chaves
print(len(pessoa))
# keys - iterável com as chaves
for chave in pessoa.keys():
    print(chave)

print(pessoa.keys)
# values - iterável com os valores
for chave in pessoa.values():
    print(chave)  # retorna os vaores

# items - iterável com chaves e valores
for chave in pessoa.items():
    print(chave)  # retorna uma tupla

# setdefault - adiciona valor se a chave não existe
pessoa.setdefault('idade', 5000) ## define um valor padrão para caso não exista

# copy - retorna uma cópia rasa (shallow copy)
import copy
print('----- copy -----\n')
d1 = {
    'c1': 1,
    'c2': 2,
    'c3': 3,
    'c4': 4,
    'l1': [0,1,2,3,3]
}

d2 = d1.copy() ## copia raza, copia somente os valores imutaveis e os mutaveris faz somente referencia do endereço da memoria, ou seja, compartilham do mesmo local 

d2['c1'] = 200 ## alterando um valor imutavel ou seja vai entrar somente para o novo local

print(d1)
print(d2)

## agora par  tem uma copia completa e total idependente tem que fazer um deepCopy

d2 = copy.deepcopy(d1)
print('Copia completa')
print(d2)

# get - obtém uma chave
print('----- GET ------ \n')
print(pessoa)

print(pessoa.get('nome', 'Jerimel')) # passando valor defat
# pop - Apaga um item com a chave especificada (del)
print('\n---- Pop ----\n')

nome = pessoa.pop('nome') # Atribui o nome a variavel tirando ela do dicionario
print(f'varaivel retirada com pop: {nome}')
print('Agora ta sem a chave que tiramos')
print(pessoa)

# popitem - Apaga o último item adicionado
print('\n ----- popitem ---- \n')
print(pessoa)
print('Agora vamos fazer um popitem que arranca o ultimo item')
pessoa.popitem() # remove o ultimo item do dicionario
print(pessoa)

# update - Atualiza um dicionário com outro
print('\n ----- update ----- \n')
print(pessoa)

tupla = (('chave', 'valor'), ('idade', 79))

pessoa.update(tupla)  ## update pode tanto atualizar como adicionar o valor se não existir

print(pessoa)
