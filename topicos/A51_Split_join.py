'''

split divide uma string
join une uma string

'''

texto = 'Lá ele mil vezes meu amigo!'
lista_texto = texto.split()

for i, texto in enumerate(lista_texto):
    print(lista_texto[i].strip())

print(lista_texto)

## passando variavel para o split (chave do que ele vai usar pra cortar)
texto = 'Lá ele   mil    vezes,    meu    amigo!'
lista_texto = texto.split(',')
novalista = []
for i, texto in enumerate(lista_texto):
    novalista.append(lista_texto[i].strip())


## passando variavel para o split (chave do que ele vai usar pra cortar)
texto = 'Lá ele   mil    vezes,    meu    amigo!'
lista_texto = texto.split()
novalista = []
for i, texto in enumerate(lista_texto):
    novalista.append(lista_texto[i].strip())

# passa a string de união deles  que no caso é o ' '
print(' '.join(novalista))





