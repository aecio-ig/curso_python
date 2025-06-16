from argparse import ArgumentParser

parser = ArgumentParser()

# quando passado agumento verboso no codigo será considerado o verboso
parser.add_argument(
    '-b',
    '--basic', 
    help='Mostra minha mensagem de help',
    required=True,
    nargs='+'
    )
# nargs faz uma lista com os argumentos passados
args = parser.parse_args()


if args.basic is None:
    print('Voce n passou o basic')
else:
    print(f'O valor passado foi {args.basic}')

print(args.basic)
