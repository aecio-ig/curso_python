
class Pessoa:
    ano_atual = 2025 ## <----- Atributo da classe altera de um altera para todos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @classmethod
    def metodos_de_classe(cls):
        print('Alou')
    
    @classmethod
    def get_ano_nascimento (self):
        return Pessoa.ano_atual - self.idade
    
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anonimo', idade)


p1 = Pessoa('Aecio', 25)

# pode ser chamada dos dois jeitos
p1.metodos_de_classe()
# Pessoa.metodos_de_classe(p1) # se não feito o decorator de class method seria necessario ser assim
Pessoa.metodos_de_classe() 


p2 = Pessoa.criar_com_50_anos('joão')
p3 = Pessoa.criar_anonimo(50)

print(p1.nome)
print(p2.nome)
print(p3.nome)


# p2 = Pessoa('Juao', 98)
# p3 = Pessoa('MAria', 58)




