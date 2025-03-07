# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho = 'C:\\Users\\62402-aecio\\Desktop\\Aecio\\'
caminho += 'arquivo.txt'

try:
    arquivo = open(caminho, 'r') ## n funciona então usamos o w

except FileNotFoundError:
    print('N achou vamos criar')
    arquivo = open(caminho, 'w') ## n funciona então usamos o w

finally:
    arquivo.close()


## context manager já abre e fecha automatico
with open(caminho, 'w+') as arquivo: ## w apaga tudo
    print('Abrimos com o with !')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    arquivo.writelines(('Linha adicional', 'MEsma linha linha adicional'))
    arquivo.seek(0,0) ## move o cursor para posição zero no arquivo
    print(arquivo.read())


## modos de abertura
with open(caminho, 'a+', encoding='utf8') as arquivo: ## em modo append ou seja vai permitir que alteremos o arquivo sem pagar tudo , passar sempre o encoding pra evitar problemas
    print('Abrimos com o with Atenção !')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    arquivo.writelines(('Linha adicional', 'MEsma linha linha adicional'))
    arquivo.seek(0,0) ## move o cursor para posição zero no arquivo
    print(arquivo.read())


import os
os.remove(caminho)


os.rename(arquivo, 'nome_do_novo_arquivo_ou_caminho_novo')

