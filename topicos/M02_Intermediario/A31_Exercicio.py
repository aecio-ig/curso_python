def soma(x,y):
    return x + y

def multiplica(x,y):
    return x * y

## função que cria função
def criar_funcao(funcao, x):
    ## cria outra dentro do escopo que espera um outro parametro que deve ser passado quando ela for chamada
    def func_interna(y):
        ## retorna a função executando
        return  funcao(x, y)
    ## a função criar função retorna a função interna sem executar ou seja, quando for chamar ela tem que chamar a variavel que foi atribuida com () que é basicamente closure
    return func_interna

soma_com_cinco = criar_funcao(soma,5)
multiplica_por_dez= criar_funcao(multiplica, 10)

print(soma_com_cinco(3))
print(multiplica_por_dez(2))

