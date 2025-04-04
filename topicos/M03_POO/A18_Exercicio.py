# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def fabricante(self):
        return self._fabricante() 
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
        print(f'A fabricante do {self.nome} agora é {fabricante.nome}')

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor
        print(f'Colocou o motozão {motor.nome} no {self.nome}')

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

## Carros
uno = Carro('uno')
hemi440 = Motor('hemi404')
fiat = Fabricante('Fiat')

uno.motor = hemi440
uno.fabricante = fiat


# saveiro = Carro('saveiro')

## Motores


# plastico = Motor('plastico')
# ferrari1 = Motor('ferrari1')

# ## Fabricantes
# eu = Fabricante('eu')
# tu = Fabricante('tu')
# elo = Fabricante('elo')






