variavel = 'ABC'

print(f'{variavel: >10}') ## Define o tamanho da string em 10 e preenche com espaço a direita
print(f'{variavel: <10}') ## DEfine o tamanho da string em 10 e preenche com espaço a esquerda
print(f'{variavel: ^10}') ## Centraliza a string de acordo com o tamanho passado
print(f'{variavel:*^10}') ## Passando o caractere ele preenchue com o char passado
print(f'{-1500.3556521248:0=+10,.1f}') ## Formata string de forma que tenha casas decimais pontos e virgulas
print(f'o hexadecimal de 1500 é {1500:08x}')## Mostrahexadecimal minusculo 
print(f'o hexadecimal de 1500 é {1500:08x}')## mosta hexadecimal maiusculo
