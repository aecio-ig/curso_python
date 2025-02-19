condicao = False

passou_no_if = None
if condicao:
    passou_no_if = True
    print('Faz algo')
else: 
    print('Nao faz algo')


print("Nao passou no if: ", passou_no_if is None)
print("Passou no if: ", passou_no_if is not None)


