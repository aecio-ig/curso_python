import sys


print(sys.argv)

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Não foi passado argumento')
