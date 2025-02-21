def imprimir(a,b,c):
    print(a)
    print(b)
    print(c)

imprimir('1', 800, 3.0)
imprimir('1', 15, 3.0)
imprimir('1', 5, 3.0)
imprimir('1', 2, 3.0)



## Passando valor padrão

def nova_func(a= 'Aecio'):
    print('Oi,  ',a)


nova_func()
nova_func('Tiago')
nova_func('Tomate')