class MeuErro(Exception):
    ...


def levantar():
    erou = MeuErro('Ihihihihi', 'a', 'b')
    erou.add_note('Voce é inteligente, não seja não inteligente!')
    raise erou

try:
    levantar()
except (MeuErro, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print(error)
    raise