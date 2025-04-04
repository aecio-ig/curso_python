

# def recursiva(inicio=0, final=10):
#     #caso recursivo, conta até o final
#     if inicio >= final:
#         return final

#     inicio += 1
#     return recursiva(inicio, final)

# print(recursiva(1,50))

def fatorial(n):
    if n <= 1:
        return 1 
    n * n-1
    return n* fatorial(n - 1)

print(fatorial(15))
print(fatorial(150))
# print(fatorial(3000))