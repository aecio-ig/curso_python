from abc import ABC, abstractmethod

class LogAbstract(ABC): ## n é pra se usado
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    @abstractmethod
    def name(self):
        return self._name



    
class Log(LogAbstract):# 
    def __init__(self, name):
        super().__init__(name)
        print('Faço nada pois chameni o super 🦸')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    ##### 
    # pode ser setado diretamente no abstract diretamente se a 
    # property estiver definida somente na abstração
    @LogAbstract.name.setter
    def name(self, name):
        self._name = name


    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


l = Log('Logqueiro')
print(l.name)