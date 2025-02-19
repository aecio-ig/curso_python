variavel = 'O homem Macaco!'
print(variavel[4:]) ## pega a partir de até final (omissoa de valor)
print(variavel[3:5]) ## Passa parte da string que quer pegar
print(variavel[:5]) ## Passa parte da string que quer pegar
## pode ser usado os index negativos
print(variavel[-4:]) ## pega a partir de até final (omissoa de valor)
print(variavel[-3:-5]) ## Passa parte da string que quer pegar
print(variavel[:-5]) ## Passa parte da string que quer pegar

# pega variavel em passo um pedaço da string pulando os pedaços
texto = 'Aqui um teste de passo pra mostrar que ele pega a string em pedaços 1234567890'
print(texto)
print(texto[3::2])
print(texto[3:15:2]) #somente do index 3 ao 15 pulando de 2 index 


# obtem o tamanho
print(len(variavel))