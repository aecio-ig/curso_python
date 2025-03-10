class Camera:
    def __init__(self, nome, filmando = False):
        self.filmando = filmando
        self.nome = nome

    def filmar(self):
        if self.filmando:
            print(f'O {self.nome} já está filmando!')
            return
        
        print(f'A {self.nome} agora está filmando!')
        self.filmando = True
    
    def fotografar(self):
        if self.filmando:
            print(f'A {self.nome} está filmando impossivel fotografar!')
            return
        print('Fotografia ticlick 📸')

    
    
c1 = Camera('Canon')
c1.fotografar()
c1.filmar()

