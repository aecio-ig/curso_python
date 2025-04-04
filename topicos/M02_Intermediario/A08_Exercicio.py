# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def duplicar(n):
    return n * 2

def triplicar(n):
    return n * 3

def quadriplicar(n):
    return n * 4

print(duplicar(2))
print(triplicar(3))
print(quadriplicar(4))



def criar_multiplicador(multipicador):
    def multiplicar(numero):
        return numero * multipicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(quadriplicar(4))