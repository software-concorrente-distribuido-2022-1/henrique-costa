import socket
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

class Server:

    def __init__(self, port, messageMaxSize):
        self.port = port
        self.messageMaxSize = messageMaxSize
        self.dep = Deposito()
    
    def start_server(self):
        host = socket.gethostname() # obter o host, como ambos os códigos estão sendo executados localmente

        server_socket = socket.socket()  # obter socket
        server_socket.bind((host, self.port))  # ligar host e a porta

        print('Servidor iniciado em ' + str(host))

        server_socket.listen(6) # escutar por até 6 clientes

        while True:
            connection, address = server_socket.accept()  # aceitar nova conexão
            t = threading.Thread(target=self.new_client, args=(connection, address)) # iniciar uma nova thread para a conexão
            t.setDaemon(True)
            t.start()

    def new_client(self, connection, address):
        print('Conexão de: ' + str(address))

        while True:
            data = connection.recv(self.messageMaxSize).decode() # obter mensagem
            if not data:
                # parar se não receber dados / a conexão for encerrada pelo cliente
                break
            if data == 'colocar':
                qtd = self.dep.colocar()
            elif data == 'retirar':
                qtd = self.dep.retirar()

            connection.send(qtd.encode()) # retornar resposta

        connection.close()  # encerrar a conexão
        print('Conexão com '+str(address)+' encerrada')

server = Server(5000, 1024)
server.start_server()