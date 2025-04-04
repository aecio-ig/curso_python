def fora(x):
    a = x  ### variavel livre
    
    def dentro():
        return a 
    return dentro


dentro1 = fora(1)
dentro2 = fora(2)

print(dentro1)
print(dentro2)


print(dentro1())
print(dentro2())


### uso de nomlocal
def concatenar(string_inicial):
    valor_final = string_inicial

    def concatenador(valor_a_concatenar=''): # diferente de global a gente vai passar o nomlocal para buscar a variavel no escopo acima ou seja não é scopo da aplicação
        nonlocal valor_final # declara que a variavel do escopo anterior pertence ao local.
        valor_final += valor_a_concatenar
        return valor_final
    return concatenador

texto = concatenar('i')
#agora texto é uma função que espera um parametro que espera o valor para concatenar
print(texto('HAHA'))

print (texto)