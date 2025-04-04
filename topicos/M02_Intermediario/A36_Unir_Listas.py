def zipper(lista1, lista2):
    print(min(1,2))
    print(min(100,200))
    intervaor_maximo = min(len(l1), len(l2))
    return [(lista1[i], lista2[i]) for i in range(intervaor_maximo)]


l1 = ['Salvador', 'pernambuco']
l2 = ['PA', 'BR', 'Minecraft']
print(zipper(l1,l2))


print(list(zip(l1,l2)))


## itera da lista de forma invertida trazendo os valores lado a lado ingluindo a maior lista
from itertools import zip_longest

print(list(zip_longest(l1,l2)))
print(list(zip_longest(l1,l2, fillvalue='Valor padrão')))

