
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} - {self.y}'


    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        r_self = self.x + self.y
        routher = other.x + other.y
        return r_self > routher


p1 = Ponto(1,3)
p2 = Ponto(15, 60)

print(p1)
print(repr(p2))
print(f'{p2!r}')

print(p1 > p2)