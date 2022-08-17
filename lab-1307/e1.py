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
            self.recurso.setTexto(self.nomeThread)
            time.sleep(0.03)
            self.recurso.mostraTexto()

recurso = Tela()

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

Nesse experimento podemos perceber claramente a concorencia de recurso pelas threads.
Uma thread seta seu texto no buffer para poder printa-lo, mas como apos setar o texto 
no buffer a thread da um sleep, nesse meio tempo enquanto ela esta 'dormindo' outra thread
já setou seu texto no buffer, então apos 'acordar' a theread imprime o texto do buffer mas 
o texto que ela imprime ( e que estava no buffer nesse momento) já não é mais o texto que
ela setou, e sim o texto que outra thread setou enquanto a outra 'dormia'.
Fica mais facil de perceber esse comportamento ao printar o nome da thered que esta imprimindo 
o texto do buffer logo antes de imprimir o texto do buffer.

Resultado:
Thread-2 imprimindo: Usuário 3
Thread-1 imprimindo: Usuário 2
Thread-3 imprimindo: Usuário 3
Thread-5 imprimindo: Usuário 2
Thread-4 imprimindo: Usuário 3
Thread-3 imprimindo: Usuário 4
Thread-2 imprimindo: Usuário 4
Thread-5 imprimindo: Usuário 4
Thread-1 imprimindo: Usuário 4
Thread-4 imprimindo: Usuário 5
Thread-5 imprimindo: Usuário 4
Thread-4 imprimindo: Usuário 4
Thread-2 imprimindo: Usuário 4
Thread-3 imprimindo: Usuário 4
Thread-1 imprimindo: Usuário 4
Thread-4 imprimindo: Usuário 1
Thread-2 imprimindo: Usuário 1
Thread-5 imprimindo: Usuário 1
Thread-1 imprimindo: Usuário 5
Thread-3 imprimindo: Usuário 5
Thread-5 imprimindo: Usuário 3
Thread-2 imprimindo: Usuário 3
Thread-4 imprimindo: Usuário 3
Thread-3 imprimindo: Usuário 3
Thread-1 imprimindo: Usuário 3
"""