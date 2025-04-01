# Polimorfismo em Python Orientado a Objetos
 # Polimorfismo é o princípio que permite que
 # classes deridavas de uma mesma superclasse
 # tenham métodos iguais (com mesma assinatura)
 # mas comportamentos diferentes.
 # Assinatura do método = Mesmo nome e quantidade
 # de parâmetros (retorno não faz parte da assinatura)
 # Opinião + princípios que contam:
 # Assinatura do método: nome, parâmetros e retorno iguais
 # SO"L"ID
 # Princípio da substituição de liskov
 # Objetos de uma superclasse devem ser substituíveis
 # por objetos de uma subclasse sem quebrar a aplicação.

from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mesagem = mensagem

    @abstractmethod
    def enviar() -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print(f'Email enviado do [{self.__class__.__name__}] com a mensagem: {self.mesagem}')
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print(f'SMS enviado do [{self.__class__.__name__}] com a mensagem: {self.mesagem}')
        return True


# n = NotificacaoEmail('Texto da notificação boladinha')
# n.enviar()

def notificar(notificacao: str):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificacao enviada')
    else:
        print('Notificacao não enviada')

notificacao_emial = NotificacaoEmail('Teste notificacao email')
notificar(notificacao_emial)

notificacao_sms = NotificacaoSMS('Teste notificacao SMS')
notificar(notificacao_sms)
