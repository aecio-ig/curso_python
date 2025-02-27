def generator(n=0):
    return 1


gen = generator(n=0)
print(gen)


## toa generator usa o yield


def generator(n=0):
    yield 1
    print('Continuando ... ')
    yield 2
    print('Continuando depois da segnda pausa')
    yield 3
    print('Executamos o ultimo...')
    return 'Acabou'


gen = generator(n=0)
for n in gen:  ## gen vira tipo uma função passo a passo 
    print(n)
## Interessante que o return n é executado




def generator2(n=0, max=1000):
    while True:
        yield n 
        n += 1

        if n >= max:
            return
        
gen = generator2(max=1000000)
for n in gen:
    print(n)