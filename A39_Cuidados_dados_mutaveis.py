## imutavel
## ele copia a variavel, não é referenciado apontado para o mesmo item na memoria
nome = 'Cleber'

outra_variavel = nome
print(outra_variavel)


nome = 'João'

print(outra_variavel)
print(nome)



### 
lista1 = [1,2,4]
lista2 = lista1   ### dessa forma ele referencia o endereço do objeto

lista2 = lista1.copy() ## dessa forma ele copia o objeto fazer um novo na memoria

lista1[0] = 'NaNs'
print(lista2)