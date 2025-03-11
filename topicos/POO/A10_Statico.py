## Metodos estaticos
class Classe:
    @staticmethod
    def funcao_dentro_classe(*args, **kwargs):
        print('oi', *args, **kwargs )

c1 = Classe()
c1.funcao_dentro_classe(1,2,3, 5)
