salas = [
    ['maria', 'joão'],
    ['pedro', 'thiago'],
    ['pimento', 'calabreso']
]

print(salas)
print(salas[0])
print(salas[2][1])


for sala in salas:
    print(sala)



for i, sala in enumerate(salas):
    print (i)
    print(i, sala[1])