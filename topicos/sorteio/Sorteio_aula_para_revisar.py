from pathlib import Path
import random

def listar_arquivos(caminho_raiz):
    return [str(arquivo) for arquivo in Path(caminho_raiz).rglob('*.py') if arquivo.is_file()]

def sortear_arquivo(caminho_raiz):
    arquivos = listar_arquivos(caminho_raiz)
    return random.choice(arquivos) if arquivos else None  # Retorna None se não houver arquivos

print('Aprenda: '+ sortear_arquivo('.') + ', e não seja Asno!')


