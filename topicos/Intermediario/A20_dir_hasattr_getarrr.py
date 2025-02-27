###

string = 'Aecio'

print(string)

if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())


iterable = ['eu', 'tenho', '__iter__']

### iterator 

iterator = iterable.__iter__() 

## chama mais bonitinho
interator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))## aqui deve dar erro


print('#### generator ####')


### generator
## são funções que sabem pausar em determinadas ocasioes
## generator <> interator 
import sys
lista = (n for n in range(10000))
generator = [n for n in range(10000)]

print(sys.getsizeof(generator))
print(sys.getsizeof(lista))


## o generator limita os dados na memoria mas n tem todos os dados na 
# memoria como algumas especificidades que tem no iterator que ja está tudo carregado na memoria
