from threading import Thread, Lock
import time



class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        time.sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('t1', 5)
t1.start()

t2 = MeuThread('t2', 5)
t2.start()


t3 = MeuThread('t3', 5)
t3.start()

while t1.is_alive():
    print('Esperando a thread')
    time.sleep(1)

for i in range(20):
    print(i)
    time.sleep(1)



class Ingressos:
    """
    Classe que vende ingressos
    """

    def __init__(self, estoque: int):
        """ Inicializando...

        :param estoque: quantidade de ingressos em estoque
        """
        self.estoque = estoque
        # Nosso cadeado
        self.lock = Lock()

    def comprar(self, quantidade: int):
        """
        Compra determinada quantidade de ingressos

        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        """
        # Tranca o método
        self.lock.acquire()
        try:
            if self.estoque < quantidade:
                print('Não temos ingressos suficientes.')
                return

            time.sleep(1)

            self.estoque -= quantidade
            print(f'Você comprou {quantidade} ingresso(s). '
                f'Ainda temos {self.estoque} em estoque.')
        finally: 
            # Libera o método
            self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)