from log import LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self.nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False
        
class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self.nome} está ligado'
            self.log_succes('Ligamos o negocio')
    
    def desligar(self):
        super().desligar()

        if self._ligado:
            msg = f'{self.nome} está desligad'
            self.log_error(msg)