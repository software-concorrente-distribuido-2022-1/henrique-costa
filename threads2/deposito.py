import threading
import time

class Deposito:
    itens = 0
    capacidade = 5
    podeRetirar = False
    podeColocar = True
    monitor = threading.Condition()

    def retirar(self):
        with self.monitor: #equivalente a "syncronized"

            if not self.podeRetirar:
                print('[ESPERA] Consumidor esperando para retirar...\n')
                self.monitor.wait()

            if (self.itens > 0):
                self.itens -= 1
                print('[RETIRADA] Caixa retirada: Sobram '+str(self.itens)+' caixas');
                self.podeColocar = True

            if (self.itens == 0):
                self.podeRetirar = False

            print('[FINAL] Consumidor terminou de retirar. podeRetirar = '+str(self.podeRetirar)+'; podeColocar = '+str(self.podeColocar)+'\n')

            self.monitor.notify()
            
    def colocar(self):
        with self.monitor: #equivalente a "syncronized"

            if not self.podeColocar:
                print('[ESPERA] Produtor esperando para colocar...\n')
                self.monitor.wait()

            if (self.itens < self.capacidade):
                self.itens += 1
                print('[ARMAZENADA] Caixa armazenada: Passaram a ser '+str(self.itens)+' caixas');
                self.podeRetirar = True

            if (self.itens == self.capacidade):
                self.podeColocar = False

            print('[FINAL] Produtor terminou de colocar. podeRetirar = '+str(self.podeRetirar)+'; podeColocar = '+str(self.podeColocar)+'\n')

            self.monitor.notify()

class Produtor(threading.Thread):

    def __init__(self, d, t):
        threading.Thread.__init__(self)
        self.dep = d
        self.tempo = t

    def run(self):
        while not parar:
            time.sleep(self.tempo)
            self.dep.colocar()
            
class Consumidor(threading.Thread):

    def __init__(self, d, t):
        threading.Thread.__init__(self)
        self.dep = d
        self.tempo = t

    def run(self):
        while not parar:
            time.sleep(self.tempo)
            self.dep.retirar()

dep = Deposito()
prod = Produtor(dep, 2)
cons = Consumidor(dep, 1)
# prod1 = Produtor(dep, 1)
# cons1 = Consumidor(dep, 5)

parar = False

prod.start()
cons.start()
# prod1.start()
# cons1.start()

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    parar = True