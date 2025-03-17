## Abstração
class Log:
    def _log(self, msg):
        raise NotImplementedError('NÃO QUERO QUE VOCE USE A CLASSE PRINCIPAL')

    # o que deve ser usado
    def log_error(self, msg): # as subclasses vao ter acesso a esses metodos pois eles não saõ protected nem privates
        return self._log(f'Error: {msg}')
    
    def log_succes(self, msg):
        return self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self, msg): # não usado
        print('LOG: ', msg)


class LogPrintMixin(Log):
    def _log(self, msg): ## não usado
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_succes('Sucesso')
    l.log_error('Erro')



