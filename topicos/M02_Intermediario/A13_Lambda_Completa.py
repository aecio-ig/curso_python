def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

print(
    executa(
        lambda x,  y: x + y, 2 , 3 ## função soma facilitada com lambda
    ),
    executa(
        soma,2,3
    ),
    soma(2,3)
)


## a lambda é para rapido e falcil, mas por padroes devemos usar função
