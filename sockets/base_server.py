import socket
from threading import Thread

class Server:

    def __init__(self, port, messageMaxSize):
        self.port = port
        self.messageMaxSize = messageMaxSize
    
    def start_server(self, callback):
        host = socket.gethostname() # obter o host, como ambos os códigos estão sendo executados localmente

        server_socket = socket.socket()  # obter socket
        server_socket.bind((host, self.port))  # ligar host e a porta

        print('Servidor iniciado em ' + str(host))

        server_socket.listen(5) # escutar por até 5 clientes

        while True:
            connection, address = server_socket.accept()  # aceitar nova conexão
            t = Thread(target=self.new_client, args=(connection, address, callback)) # iniciar uma nova thread para a conexão]
            t.setDaemon(True)
            t.start()

    def new_client(self, connection, address, callback):
        print('Conexão de: ' + str(address))

        while True:
            data = connection.recv(self.messageMaxSize).decode() # obter mensagem
            if not data:
                # parar se não receber dados / a conexão for encerrada pelo cliente
                break

            message = callback(data) # executar função
            connection.send(message.encode()) # retornar resposta

        connection.close()  # encerrar a conexão
        print('Conexão com '+str(address)+' encerrada')