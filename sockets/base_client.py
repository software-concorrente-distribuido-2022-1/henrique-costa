import socket

class Client:

    def __init__(self, port, messageMaxSize):
        self.port = port
        self.messageMaxSize = messageMaxSize
        self.host = socket.gethostname() # obter o host, como ambos os códigos estão sendo executados localmente
        self.client_socket = socket.socket()  # obter socket

        self.client_socket.connect((self.host, self.port))  # conectar ao servidor
    
    def send_message(self, message):
        self.client_socket.send(message.encode())  # enviar mensagem

        data = self.client_socket.recv(self.messageMaxSize).decode() # obter mensagem
        if not data:
            return '-'
        return data
    
    def close_connection(self):
        self.client_socket.close()  # encerrar conexão