import sys
sys.path.append('caminho para importaçãos')
... # apos isso pode importar os modulos do endereco 

import A26_Moduacao_m
print('Este modulo se chama:', __name__)
print(*sys.path, sep='\n')