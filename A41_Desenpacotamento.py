nome1, nome2, nome3 = ['Maria', 'João', 'Pedro']

print(nome2)


nome1, nome2, *resto = ['Maria', 'João', 'Pedro', 'Ananias']
## atribui a variavel aos que querem e atribui o resto a outra variavel que recebe as não atribuidos
print(resto)


## ignora o resto
nome1, nome2, *_ = ['Maria', 'João', 'Pedro', 'Ananias']

## pode tb fazer assim
_, _, nome1, *_ = ['Maria', 'João', 'Pedro', 'Ananias']