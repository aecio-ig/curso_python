"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
def printLista():
    if len(lista) < 1:
        print('Lista vazia!')
    else:
        print('---Lista---')
        for i, item in enumerate(lista):
            print(i, item)
lista = []
print("Vamos as compras tião?")
while True:
    comando = input('[I]nserir [A]pagar [L]istar: ').lower().strip()

    if comando not in ['i', 'a', 'l']:
        print('Digite um comando valido!')
        continue

    if comando == 'a':
        if len(lista) > 0:
            printLista()
        else:
            print('Lista está vazia!')
            continue
        
        index = input('\n Informe o numero do item que deseja remover: ')
        try:
            index = int(index)
            del lista[index]
            print('Deletado com sucesso!')
        except TypeError: 
            print('Informe um valor valido!')
        except IndexError: 
            print('Produto não está na lista!')
        except: 
            print('Erro desconhecido!')


    if comando == 'i':
        produto = input('Qual produto deseja inserir: ')
        if produto not in lista:
            lista.append (produto)
            printLista()
        else:
            print('Produto informado já foi adicionado a lista!')
            printLista()
            continue

    if comando == 'l':
        printLista()