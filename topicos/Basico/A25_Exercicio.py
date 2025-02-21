"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome_usuario = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome_usuario == '' or idade == '':
    print('Desculpe, você deixou campos vazios.')
else:
    print(f'Seu nome é {nome_usuario}')
    print(f'Seu nome invertido é {nome_usuario[::-1]}')
    print(f'Primeira letra do seu nome é: {nome_usuario[0]}')
    print(f'A ultima letra do seu nome é: {nome_usuario[len(nome_usuario)-1]}')
    print(f'A ultima letra do seu nome é: {nome_usuario[-1:]}')
    print('Seu nome contem espaço' if ' ' in nome_usuario else 'Seu nome não contem espaços')
    print('Seu nome tem:', len(nome_usuario))