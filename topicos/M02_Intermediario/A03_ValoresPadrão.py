def soma(x, y, z = 5):
    return x+y+z

print(soma(1,2))



def soma2(x, y, z = None):
    if z is not None:
        return y+z
    else:
        return x+y

print(soma2(1,2))