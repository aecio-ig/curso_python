class MeuErro(Exception):
    ...


def levantar():
    erou = MeuErro('Ihihihihi', 'a', 'b')
    raise erou

try:
    levantar()
except (MeuErro, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print(error)