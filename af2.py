"""
    Henrique Martins Costa - 201905533
    Artur Rocha Lapot - 201905524
"""

import threading
import time
import random, string

#função para gerar uma palavra aleatória do tamanho especificado
def randomWord(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class MailBox:
    message = None
    monitor = threading.Condition()

    def retrieveMessage(self):
        with self.monitor: #equivalente a "syncronized"

            if self.message == None:
                print('[ESPERA] Nenhuma menssagem recebida. ' + threading.current_thread().name + ' está esperando\n') 
                self.monitor.wait()

            if self.message != None:
                print('[RETRIEVED] Menssagem: "' + self.message + '" - Recebida por: ' + threading.current_thread().name + '\n')
                self.monitor.notify()
                returnMessage = self.message
                self.message = None #apagar mensagem atual
                return returnMessage
            
    def storeMessage(self, newMessage):
        with self.monitor: #equivalente a "syncronized"

            if self.message != None:
                print('[ESPERA] Producer ' + threading.current_thread().name +' esperando para escrever nova menssagem' + '\n')
                self.monitor.wait()

            if self.message == None:
                print('[STORED] Mensagem: "' + newMessage + '" - Armazenada por: ' + threading.current_thread().name + '\n')
                self.message = newMessage

            self.monitor.notify()

class Producer(threading.Thread):

    def __init__(self, nome, m):
        threading.Thread.__init__(self)
        self.name = nome
        self.mail = m

    def run(self):
        while not parar:
            time.sleep(2)
            palavra = randomWord(random.randint(3, 10))
            self.mail.storeMessage(palavra + ' - Enviado por ' + self.name)
            
class Consumer(threading.Thread):

    def __init__(self, nome, m):
        threading.Thread.__init__(self)
        self.name = nome
        self.mail = m

    def run(self):
        while not parar:
            time.sleep(2)
            self.mail.retrieveMessage()

mail = MailBox()
prod = Producer('Produtor 1', mail)
cons = Consumer('Consumidor 1', mail)
prod1 = Producer('Produtor 2', mail)
cons1 = Consumer('Consumidor 2', mail)

parar = False

prod.start()
cons.start()
prod1.start()
cons1.start()


#esta parte do código só serve para parar as threads ao interromper com o teclado (se não é preciso matar o terminal)
try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    parar = True