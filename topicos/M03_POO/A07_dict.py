

class Pessoa:
    ano_atual = 2025 ## <----- Atributo da classe altera de um altera para todos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    
    def get_ano_nascimento (self):
        return Pessoa.ano_atual - self.idade
    

aecio = Pessoa('Aecio', 25)
juao = Pessoa('Juao', 98)

print(aecio.get_ano_nascimento())
print(juao.get_ano_nascimento())        

## a classe contem um dict com tudo dela
print(aecio.__dict__)