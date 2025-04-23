from pathlib import Path

caminho_projeto = Path()

print(caminho_projeto)
print(caminho_projeto.absolute())


## pegar camiho atual
caminho_arquivo = Path(__file__)
print(caminho_arquivo)

## para ver o pai do arquivo atual é
print(caminho_arquivo.parent.parent.parent.parent)

## gerar um novo caminho
ideias = caminho_arquivo.parent / 'ideias'
print(ideias)


## pra pegar a home geralmente usuarios
print(Path.home())


## ele pega o que era somente o caminho e gera o arquivo
ideias.touch() 

## escrever no arquivo
ideias.write_text('Teste de geração de arquvio pelo python!')

## esse aqui apaga que é ao contrario do toutch
ideias.unlik()

