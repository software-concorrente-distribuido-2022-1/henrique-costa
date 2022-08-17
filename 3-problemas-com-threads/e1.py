import threading

class minhaThread (threading.Thread):
    def __init__(self, idThread, nome):
        threading.Thread.__init__(self)
        self.idThread = idThread
        self.nome = nome

    def run(self):
        print ("Iniciando contagem")
        
        #obter lock
        threadLock.acquire()
      
        for x in range(1, 101):
            print(x)
    
        #liberar lock
        threadLock.release()

threadLock = threading.Lock()

#criar a thread
thread1 = minhaThread(1, "Thread 1")

#iniciar a thread
thread1.start()

#esperar pela thread terminar
thread1.join()

#imprimir quando a thread terminar
print ("Programa finalizado")