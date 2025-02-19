'''
iteravel -> str, range, etc (__iter__)
iterador -> quem vai entregrar o valor um por vez 
next -> metodo que avança o iterador
iter -> função que entrga o iterador
'''

texto = iter("Aecio")

print(texto.__next__())
print(texto.__next__())
print(next(texto))
print(texto.__next__())
print(texto.__next__())
# print(texto.__next__()) stop iterator


texto_teste = 'Aecio'
interador = iter(texto_teste)

while True:
    try:
        letra = next(interador)
        print(letra)
    except StopIteration:
        break

