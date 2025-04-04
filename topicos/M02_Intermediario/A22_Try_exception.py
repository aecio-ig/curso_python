

try:
    a = 18
    b = 0
    # c = a/b
    # print(c)
    #Index error
    b[1]
except ZeroDivisionError:
    print('Tratamento de erro de dividido pa zero')
except TypeError as e:
    print('Tratamento de erro para type error')
    print(e.__class__.__name__)
except (TypeError, ZeroDivisionError) as error:
    print(error) ### dessa forma o erro fica instanciado
    print(error.__class__.__doc__) ### dessa forma o erro fica instanciado


    