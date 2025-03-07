def adiciona_clientes(nome, lista=[]):
    ## para resolver problema de parametros mutaveis em python
    ## para resolver ele é preciso ter cuidado e para evitar problemas de referencia de lista no momento da chamada
    ## pode ser criado a lista que vai ser retornada caso ela n seja passada na função
    if lista is None:
        lista = [] # assim criando locamente o objeto que vai ser passado
    lista.append(nome)
    return lista


cliente = adiciona_clientes('Aecio')
adiciona_clientes('Joana', cliente)
print(cliente)