import threading
import random
import time

ganhadora = None
ordemChegada = []

class lebre(threading.Thread):
    def __init__(self, idLebre, nome):
        threading.Thread.__init__(self)
        self.idLebre = idLebre
        self.nome = nome
        self.distancia = 0
        self.saltos = 0

    def run(self):

        global ganhadora

        #enquanto não tiver ganhadora
        while self.distancia < 20:

            #salto entre 1 e 3 metros
            salto = random.randint(1, 3)

            self.distancia += salto
            self.saltos += 1

            print(self.nome+' saltou '+str(salto)+' metros')

            if (self.distancia >= 20 and ganhadora == None):
                #definir como ganhadora
                ganhadora = self.idLebre

            #descansar
            time.sleep(0.0001) #equivalente a yield()

        if (self.distancia >= 20):
            ordemChegada.append(self.idLebre)

lebres = []

for i in range(5):
    nomeLebre = 'Lebre-'+str(i+1)
    l = lebre(i, nomeLebre)
    lebres.append(l)

#iniciar as lebres
for l in lebres:
    l.start()

#esperar para que todas terminem
for l in lebres:
    l.join()

if (ganhadora != None):
    print('Ganhadora: '+lebres[ganhadora].nome)
    
    #posição e saltos de cada lebre
    for i, idLebre in enumerate(ordemChegada):
        lebre = lebres[idLebre]
        print(str(i+1)+'º lugar: '+lebre.nome+' - '+str(lebre.saltos)+' saltos')