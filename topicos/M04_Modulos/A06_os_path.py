# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.


import os

caminho = os.path.join('D:', 'GIT', 'curso_python','teste.txt')
print(caminho)

# Separa arquivo do diretorio, util para manipular
diretorio, arquivo = os.path.split(caminho)
print(diretorio, arquivo)

caminho_arquivo, extencao_arquivo = os.path.splitext(arquivo)
print(caminho_arquivo, extencao_arquivo)

# verifica se existe
print(os.path.exists(caminho))

# Caminho absoluto da pasta atual
print(os.path.abspath('.'))

# parte final do caminho ultimo arquivo ou diretorio final
print(os.path.basename(caminho))
