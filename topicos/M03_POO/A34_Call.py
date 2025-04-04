# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
## é tipo quando chama a instancia da classe podendo ser chamada que é <> da classe ser chamada


class Foo:
    def __init__(self, phone):
        self.phone = phone

    
    def __call__(self, nome): 
        print(nome, ' Está chamando: ', self.phone)

call = Foo('132456')
call('Jerimeel')  