# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.


class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
    

class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome
    
    def escrever(self):
        return f'{self.nome} está escrevendo 🫢'
    
escritor = Escritor('Jerimel')
caneta = FerramentaDeEscrever('Canetinha azul')
escritor.ferramenta = caneta ##   <---- Relacionando as classes

print(caneta.escrever())
print(escritor.ferramenta.escrever()) ## <--- chama a mesma função da classe mas pela instancia da classe pricipal


