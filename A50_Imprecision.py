numero1 = 0.1
numero2 = 0.7

numero3 = numero1 + numero2
print(numero3)

print(f'{numero3:.2f}')

print(round(numero3, 2))


import decimal

numero1 = decimal.Decimal(numero1)
numero2 = decimal.Decimal(numero2)
numero3 = numero1 + numero2

print(numero3)
### n deu certo