import os
import shutil
## copia os bagui de um lugar para outro 

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')

PASTA_ORIGINAL = os.path.join(DESKTOP, 'teste')
NOVA_PASTA =  os.path.join(DESKTOP, 'teste_nova_pasta')


os.makedirs(NOVA_PASTA, exist_ok=True)


for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_arquvio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )

        os.makedirs(caminho_arquvio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_arquvio_novo  = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminho_arquvio_novo)

