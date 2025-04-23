# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

import os
from itertools import count


caminho = os.path.join(os.path.abspath('.'))

counter = count()

for root, dirs, files in os.walk(caminho):
    counteror = next(counter)
    print(counteror, root)

    for dir_ in dirs:
        print(' ', counteror, 'Dir:', dir_)

    for file_ in files:
        print(' ', counteror, 'File:', file_)