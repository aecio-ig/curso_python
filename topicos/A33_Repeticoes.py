contador = 0

while contador < 100:
    if contador % 10 == 0:
        print(f'Estamos no {contador}!')
    
    contador += 1

    if contador % 6 == 0:
        print(f' {contador} é divisivel por 6 pulando essa binboca!')


linha = 0
coluna = 0
limite_linha = 10
limite_coluna = 100
caractere = '*'

while linha < limite_linha:
    linha +=1
    while coluna < limite_coluna:
        coluna +=1 
        print(caractere*coluna)
    