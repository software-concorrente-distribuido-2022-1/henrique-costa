import threading
from typing import List
import numpy
import time

class ArrayParallelSearch:

    def threadSearcher(self, x: int, index: int, a: List[int], resultado):
        threadAtual = threading.current_thread()

        for i, value in enumerate(a):

            if(len(resultado) > 0):
                print('Parando '+threadAtual.name+' em i='+str(i))
                break

            #se achou o valor da busca
            if (value == x):
                resultado.append(i+index) #resultado será o índice do array original, então: índice do array atual mais o deslocamento dele
                print('Encontrado o valor na '+threadAtual.name)
                break

            #permitir que as outras threads realizem um ciclo de busca
            time.sleep(0.0001) #equivalente a yield()

    def parallelSearch(self, x: int, a: List[int], numThreads: int):
        threads = []
        resultado = []
        index = 0

        #dividir o array para a quantidade de threads
        divisoes = numpy.array_split(a, numThreads)

        #criar uma thread para cada array resultante da divisão
        for arr in divisoes:
            arrSize = len(arr)

            if (arrSize > 0):
                t = threading.Thread(target=self.threadSearcher, args=(x, index, arr, resultado))
                threads.append(t)

            #incrementar o índice (desclocamento) com a quantidade de elementos do array atual
            index += arrSize

        #iniciar as threads
        for t in threads:
            t.start()
        
        #esperar para terminem ou parem
        for t in threads:
            t.join()

        #retornar o índice se encontrou o valor, ou -1 caso contrário
        if (len(resultado) > 0):
            return resultado[0]
        else:
            return -1


arrayParallelSearch = ArrayParallelSearch()

#i = arrayParallelSearch.parallelSearch(13, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 4)

#gerar um array de 100 números aleatórios de 1 a 200
randnums = numpy.random.randint(1,200,100)

#buscar o número 42 no array, dividindo em 5 threads
i = arrayParallelSearch.parallelSearch(42, randnums, 5)

print(i)
print(randnums)