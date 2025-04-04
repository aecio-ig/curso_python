# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯


class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property ## usando property coo getter
    def cor(self):
        return self._cor
    
    @cor.setter ## usando property com setter
    def cor(self, valor):
        self._cor = valor

    
caneta = Caneta('Azul 😩')
print(caneta.cor)
caneta.cor = 'Rosinha'
print(caneta.cor)
    
