class Carro:
    def __init__(self, nome = 'Não passou valor'):
        self.nome = nome
    
    def acelera_veiculo(self):
        print(f'{self.nome} está acelerando muito, Rhan dan dan dan dan PÁ PÁ')

fusca = Carro('Fusca Potente')
print(fusca.nome)
fusca.acelera_veiculo()


celta = Carro('Celta tartaruga')
print(celta.nome)
celta.acelera_veiculo()