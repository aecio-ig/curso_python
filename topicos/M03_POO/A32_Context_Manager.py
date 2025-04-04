from contextlib import contextmanager

@contextmanager
def my_open(caminho, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho, modo, encoding='utf8')
        yield arquivo 
    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open('teste1.txt', 'w') as ist:
    ist.write('Linha 1 \n')
    ist.write('Linha 2 \n',132)
    ist.write('Linha 3 \n')
    print('With', ist)


## outro exemplo

from contextlib import contextmanager

@contextmanager
def conectar_banco():
    print("Conectando ao banco...")
    conexao = "CONEXÃO ATIVA"  # Simulando uma conexão
    yield conexao  # Entrega a conexão para o bloco 'with'
    print("Fechando conexão...")
    conexao = None  # Simulando fechamento

# Usando no 'with'
with conectar_banco() as db:
    print("Usando o banco:", db)  # Conexão ativa aqui!

# Aqui já fechou!
