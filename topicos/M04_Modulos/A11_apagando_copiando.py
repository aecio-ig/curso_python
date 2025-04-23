import os
import shutil
## copia os bagui de um lugar para outro 

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')

PASTA_ORIGINAL = os.path.join(DESKTOP, 'teste')
NOVA_PASTA =  os.path.join(DESKTOP, 'teste_nova_pasta')


shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)