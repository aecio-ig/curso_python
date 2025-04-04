''' Closure '''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar ### retorna a função não a execução dela

s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Bom tarde')

print(s1)
print(s2('Aecio'))  #closure é aqui one executamos a função
print(s2('Jerimel'))  #closure é aqui one executamos a função


