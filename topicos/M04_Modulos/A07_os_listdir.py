import os

caminho = os.path.join(os.path.abspath('.'))
print(caminho)

# ele entra nos diretorios em camadas
for pasta in os.listdir(caminho): 
    if not os.path.isdir(pasta):
        continue

    print()
    print(pasta)
    print()

    for imagem in os.listdir(pasta):
        print(imagem)