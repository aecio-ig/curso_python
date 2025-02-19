string = 'AECIO LUCIO'
lista = [123, True, 'Aecio', 1.2] ## Permite inserir qualquer tipo

print(lista)
print(lista[1], type(lista[1]))

## deleta item da lista

del lista[1]
print(lista)

## adiciona item na lista
lista.append('Valor apenddado')

## Remove do final
lista.pop()
print(lista)



lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

## Concateção 
lista3 = lista1 + lista2

print(lista3)

## Muda informação do lista1 adicionando a lista 2 a ele
lista1.extend(lista2)

print(lista1)