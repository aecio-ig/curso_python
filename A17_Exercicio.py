valor1 = input('Digite primeiro valor: ')
valor2 = input('Digite o segundo valor: ')

if valor1 > valor2:
    print('Valor {} é maior que {}'.format(valor1,valor2))
elif valor1 == valor2:
    print('Valores iguais')
else: 
    print('Valor {} é maior que {}'.format(valor2,valor1))