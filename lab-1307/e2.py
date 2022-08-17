import threading
import time
import random

class Tela:
    texto = ''

    def setTexto(self, t):
        self.texto = t

    def mostraTexto(self):
        print(threading.current_thread().name+' imprimindo: '+self.texto)

class UserSemControle(threading.Thread):
    
    def __init__(self, nomeThread, recurso):
        threading.Thread.__init__(self)
        self.nomeThread = nomeThread
        self.recurso = recurso

    def run(self):

        for i in range(5):
            monitor.acquire() #solicitar acesso
            self.recurso.setTexto(self.nomeThread)
            time.sleep(0.03)
            self.recurso.mostraTexto()
            monitor.release() #liberar acesso

recurso = Tela()
monitor = threading.Lock()

qtdThreads = 5
threads = []

#criar threads
for i in range(qtdThreads):
    t = UserSemControle(('Usuário '+str(i+1)), recurso)
    threads.append(t)

#array de threads em ordem aleatória
random.shuffle(threads)

#iniciar as threads
for t in threads:
    t.start()

""" 
Henrique Martins Costa - 201905533
Artur Rocha Lapot - 201905524

Nesse experimento podemos perceber que com a implementação de um monitor
para controlar as threads a divisão do recurso entre elas fica bem melhor.
Assim que a primeira thered adquire o acesso ao recurso  com o monitor, as
demais threads não conseguem adquirir esse acesso ao recurso pelo monitor
ate que a theread que está com o acesso libere/de release do seu acesso,
e essa thread só vai fazer isso apos rodar totalmente, resolvendo assim o
problema de as threads printarem textos de outras threds em vez do texto 
que a propria setou no buffer, pois agora com o monitor, só uma thread por
vez tem acesso ao recurso.

Resultado:
Thread-5 imprimindo: Usuário 5
Thread-5 imprimindo: Usuário 5
Thread-5 imprimindo: Usuário 5
Thread-5 imprimindo: Usuário 5
Thread-5 imprimindo: Usuário 5
Thread-4 imprimindo: Usuário 4
Thread-4 imprimindo: Usuário 4
Thread-4 imprimindo: Usuário 4
Thread-4 imprimindo: Usuário 4
Thread-4 imprimindo: Usuário 4
Thread-2 imprimindo: Usuário 2
Thread-2 imprimindo: Usuário 2
Thread-2 imprimindo: Usuário 2
Thread-2 imprimindo: Usuário 2
Thread-2 imprimindo: Usuário 2
Thread-3 imprimindo: Usuário 3
Thread-3 imprimindo: Usuário 3
Thread-3 imprimindo: Usuário 3
Thread-3 imprimindo: Usuário 3
Thread-3 imprimindo: Usuário 3
Thread-1 imprimindo: Usuário 1
Thread-1 imprimindo: Usuário 1
Thread-1 imprimindo: Usuário 1
Thread-1 imprimindo: Usuário 1
Thread-1 imprimindo: Usuário 1
"""