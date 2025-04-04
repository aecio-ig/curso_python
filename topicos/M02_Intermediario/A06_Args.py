


def soma(*args):
    ## args sempre são tuplas
    print(args)
    valor = 0
    for i in args:
        valor+= i
        print(i)
    print(f'Valor  é de {valor}')
    


soma(1, 1 , 5) 


