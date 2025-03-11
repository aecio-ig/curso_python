# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        self.cor_tampa = cor

    @property ## usando property coo getter
    def cor(self):
        return self.cor_tinta

    @property # nome da função property que parece metodo mas chama property ou seja ela n é uma chamada usando ()
    def tampa(self):
        return self.tampa

###############################
# | Codigo cliente
# v

caneta = Caneta('Azul')
# print(caneta.cor)

# O correto é usarmos
print(caneta.cor)
print(caneta.tampa)



# # ---------------------------------------------
# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor

#     def get_cor(self):
#         return self.cor

# ###############################
# # | Codigo cliente
# # v

# caneta = Caneta('Azul')
# # print(caneta.cor)

# # O correto é usarmos
# print(caneta.get_cor())
