texto = 'O python é uma linguagem'\
    ' ela é boladinha, bem da bou mesmo, o python tá ai vlw!'

i = 0
maior_quantidade = 0
letra_maior_quantidade = ''
while i < len(texto):
    ## ver qual letra pareceu mais
    letra_atual = texto[i]
    count_letras_atual = texto.count(letra_atual)
    if count_letras_atual > maior_quantidade and letra_atual != ' ':
        maior_quantidade = count_letras_atual
        letra_maior_quantidade = letra_atual
    
    i += 1

print(f'A letra que apareceu pais vezes foi "{letra_maior_quantidade}", aparecendo {maior_quantidade} vezes!')

