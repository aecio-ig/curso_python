numero = input('Insira um numero para ser dobrado: ')
try:
    numero_float = float(numero)
    print('O dobro é:', numero_float * 2)
except:
    print('Não é numero inteigentão!')
