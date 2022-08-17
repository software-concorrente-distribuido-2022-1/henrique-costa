import threading
import time

class calculaPrimo(threading.Thread):
    def __init__(self, inicio, fim):
        threading.Thread.__init__(self)
        self.inicio = inicio
        self.fim = fim
        self.total = inicio - fim

    def run(self):

        primos = []

        for num in range(self.inicio, self.fim):

            ePrimo = True
            i = 2

            while (i*i) <= num:

                if (num % i) == 0:
                    ePrimo = False
                    break

                i += 1
            
            if (ePrimo and num > 1):
                primos.append(num)

                qtdPrimos = len(primos)
                if (qtdPrimos % 20000 == 0):
                    progresso = round(((self.inicio-num)*100)/self.total, 2)
                    print(self.name+' - descoberto '+str(qtdPrimos)+' primos - '+str(progresso)+'%')

        qtdPrimos = len(primos)
        print('Existem '+str(qtdPrimos)+' primos entre '+str(self.inicio)+' e '+str(self.fim))
        if (qtdPrimos > 0):
            print('Eles são: ', primos)
        print(qtdPrimos)

thread1 = calculaPrimo(1000000, 30000000)
thread2 = calculaPrimo(90000000, 120000000)

inicio = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

tempoTotal = round((time.time() - inicio), 3)
print('Tempo total para realizar os cálculos: '+str(tempoTotal)+' segundos')