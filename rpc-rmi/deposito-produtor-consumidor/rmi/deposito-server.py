import threading
import Pyro4

# lembrar de rodar "python -m Pyro4.naming" para subir o servidor de nomes

@Pyro4.expose
class Deposito(object):
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

            return str(self.itens)
            
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

            return str(self.itens)

dep = Deposito() # instanciar o depósito

daemon = Pyro4.Daemon() # fazer o deamon do Pyro
ns = Pyro4.locateNS() # obter o nome do servidor
uri = daemon.register(dep) # registrar a instancia do Deposito como um objeto do Pyro
ns.register('scp.deposito', str(uri)) # registrar o objeto com um nome no servidor/serviço de nomes (equivalente a registry)

print('Ativo. Pronto para escutar.')

daemon.requestLoop() # iniciar o loop do servidor e esperar por chamadas