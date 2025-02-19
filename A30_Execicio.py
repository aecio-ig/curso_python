"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_inteiro = input('Digite um numero inteiro: ')
if not numero_inteiro.isdigit:
    print('Não é numero inteiro 💀')
else:
    if (int(numero_inteiro) % 2) == 0:
        print('Seu numero é par!')
    else:
        print('Seu numero é impar!')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Olá plebeu que horas sõa ai? ')
if not numero_inteiro.isdigit:
    print('Não é hora 💀')
else:
    hora = int(hora)
    if hora in range(0,11):
        print('Excelente, tenha um Bom Dia!')
    elif hora in range(12,17):
        print('Excelente, tenha uma boa tarde!')
    elif hora in range(18,23):
        print('Excelente, tenha uma boa noite!')
    else:
        print('Tá de brincation with me cara ? 😩')
        
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Coé teu nome? ')
if len(nome) <=4:
    print('teu nome é litle')
elif len(nome) > 4 and len(nome) < 7: 
    print('teu nome é médio')
elif len(nome) >= 7:
    print('teu nome é very biggest')
