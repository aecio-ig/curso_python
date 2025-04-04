try:
    print('Processo 1')
    if 1 == 1:
        raise 
    print('Processo 2')

except RuntimeError as e:
    print('Erro proposital chamado')
    print(e.__class__.__name__)

finally:
    print('Aqui é o finally')

