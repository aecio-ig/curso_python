'''
enumerate é umeros iteraveis (indices)


'''


lista = ['maria', 'joao', 'pedro', 'ana']

lista.append('jose')

lista_enumerada = enumerate(lista)

## não pode fazer for aninhado usando o mesmo iterator pq ele vai ser consumido
for item in lista_enumerada:
    print(item)

## então o ideal é chamar o enumerate diretamente no for
for item in enumerate(lista):
    print(item)
    for i in enumerate(lista):
        print(i)


print('-------')
for item, nome in enumerate(lista):
    print(item, nome)