# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

tarefas_lista = []
tarefas_lixeira = []
while True:
    comandos_padrão = ['refazer', 'desfazer', 'limpar']
    comando = input('Digite alguma tarefa ou comando: ')
    if comando not in comandos_padrão:
        tarefas_lista.append(comando)

    elif comando == comandos_padrão[0]: ## refazer
        try:
            tarefas_lista.append(tarefas_lixeira[-1])
            del tarefas_lixeira[-1]
        except IndexError: 
            print('Não temos nada para refazer')
    elif comando == comandos_padrão[1]: ##desfazera
        
        try:
            tarefas_lixeira.append(tarefas_lista[-1])
            del tarefas_lista[-1]
        except IndexError: 
            print('Não temos nada para desfazer')
            
    elif comando ==  comandos_padrão[2]:
        tarefas_lista = []
    
    print('-- Lista de Tarefas --')
    for i in tarefas_lista:
        print(i)
    