

import json 
import os


NOME_ARQUIVO = 'A13_json_load.json'
CAMINHO_ABS_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

print(os.path.dirname(__file__))

