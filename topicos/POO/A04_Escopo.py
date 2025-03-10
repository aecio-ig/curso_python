class Animal:
    def __init__(self, nome):
        self.nome = nome
        
        variavel = 'valor'

        print(variavel)
            
    def comendo(self, alimento):
        print(f'O {self.nome} tá comendo {alimento}')

leao = Animal('Leão')
leao.comendo('Pombos')