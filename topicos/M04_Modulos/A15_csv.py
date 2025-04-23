from pathlib import Path
import csv

CAMINHO_CSV =  Path(__file__).parent/'aula15.csv'

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo)
    # podemos tbm chamar como dict
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)
        # podendo tambem mexer nos indices
        print(linha[0])

        print(linha['Nome'])