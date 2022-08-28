import socketserver
import threading
from xmlrpc.server import SimpleXMLRPCServer

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

class RPCThreading(socketserver.ThreadingMixIn, SimpleXMLRPCServer):
    pass

dep = Deposito()

host = '127.0.0.1'
port = 4000
server = RPCThreading((host, port), allow_none=True)
print(f'Escutando na porta {port}...')

server.register_function(dep.retirar, 'retirar')
server.register_function(dep.colocar, 'colocar')

# server.serve_forever()
t = threading.Thread(target=server.serve_forever)
t.start()