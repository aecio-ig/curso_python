# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protected'
        self.__private = 'isso é private'

    def metodo_publico(self): ## podem ser usados em qualquer lugar
        print(self.public) 

    def _metodo_protected(self): # deve ser usado somente dentro doda classe e nas suas classes filhas
        print(self._protected)
    
    def __metodo_private(self): ## deve ser usado somente dentro da classe
        print(self.__private)

    def metodo_publico_acessa_privates_na_classe(self):
        return(self.__metodo_private)    

## por fora da classe devemos acessar somente o que é publico
f = Foo()
print(f.metodo_publico_acessa_privates_na_classe())
