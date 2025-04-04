class MinhaString(str):
    def upper(self):
        print('Chamou super')
        retorno = super().upper()
        print('Usou o super')
        return retorno
        

string = MinhaString('String criadas')
print(string.upper())


print(' -- Exemplo -- ')

class A:
    def metodo(self):
        print('A')


class B(A):
    def metodo(self):
        print('B')


class C(B):
    def metodo(self):
        super()
        super(B, self).metodo() ## o super de B é o ---> A - è tipo chamar algo que ta fora do escopo
        super().metodo() # esse é a chamada no B 
        print('C')

c = C()
c.metodo()