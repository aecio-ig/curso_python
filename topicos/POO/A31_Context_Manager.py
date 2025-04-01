class MyContextManager:
    def __init__(self, caminho, modo):
        print('Enter')
        self.caminho = caminho
        self.modo = modo
        self._arquivo = None

    def __enter__(self)   :
        print('Abrindo arquivo')
        self._arquivo  = open(self.caminho, self.modo, encoding='utf8')
        return self._arquivo  

    def __exit__(self, class_exception, exception_, traceback_): # aqui é tipo um finally porem da classe
        print('Exit da class')
        print(class_exception.__class__.__name__)

    ### edição outra aula
    def __exit__(self, class_exception, exception_, traceback_): # aqui é tipo um finally porem da classe
        print('Exit da class')
        
        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        # exception_.add_note('Minha nota')
        return True
        

with MyContextManager('teste1.txt', 'w') as ist:
    ist.write('Linha 1 \n')
    ist.write('Linha 2 \n')
    ist.write('Linha 3 \n')
    print('With', ist)


