# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua , endereco.numero)
    
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
        
c1 = Cliente('Maria')
c1.inserir_endereco('Av Francisco Teobaldo', 10)
c1.inserir_endereco('Av Tião Lapela', 86)

print(c1.enderecos[0])

