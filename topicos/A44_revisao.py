"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'cadelo'.lower()
tentativas = 0 
letras_digitadas = []
while True:
    tentativas += 1
    letra = input('Digite uma letra: ').lower()
    if letra in palavra_secreta:
        letras_digitadas.append(letra)

    texto_format = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in palavra_secreta:
            texto_format += letra_secreta
        else:
            texto_format += '😂'
    print(f'Palavra: {texto_format}')
    ### incompleto depois termino 😩