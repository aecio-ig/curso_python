import json

CAMINHO_ARQUIVO = 'topicos\\POO\\A08_Salvar_classe_Json.json'


class Pessoa:
    ano_atual = 2025 ## <----- Atributo da classe altera de um altera para todos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    
    def get_ano_nascimento (self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('Aecio', 25)
p2 = Pessoa('Juao', 98)
p3 = Pessoa('MAria', 58)

db = [vars(p1), p2.__dict__,p3.__dict__]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(db,arquivo, ensure_ascii=False)

