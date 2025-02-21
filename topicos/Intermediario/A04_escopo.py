
x = 0
print(x)

def escopo():
    global x
    x = 1
    print(x)
    def outra_funcao():
        y = 2
        #print(y )

    outra_funcao()
    

escopo()

print(x)