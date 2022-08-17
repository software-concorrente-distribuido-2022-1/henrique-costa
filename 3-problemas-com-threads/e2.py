import threading
import time

class minhaThread (threading.Thread):
    def __init__(self, idThread, nome, fruta):
        threading.Thread.__init__(self)
        self.idThread = idThread
        self.nome = nome
        self.fruta = fruta

    def run(self):
        while not finished:
            print (self.fruta)

finished = False

#criar as threads
thread1 = minhaThread(1, "Thread 1", "maçã")
thread2 = minhaThread(2, "Thread 2", "abacaxi")
thread3 = minhaThread(3, "Thread 3", "laranja")
thread4 = minhaThread(4, "Thread 4", "uva")
thread5 = minhaThread(5, "Thread 5", "pêssego")

#iniciar as threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

time.sleep(3)
finished = True

print ("Finalizado")