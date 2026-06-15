
import random #David Lucas
import time

def insertionSort(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i -1
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual
        
    return lista

tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

for tamanho in tamanhos:
    l = []
    for i in range(tamanho):
        l.append(random.random())

    tempo_inicial = time.time()

    insertionSort(l)

    tempo_final = time.time()

    tempo_total = tempo_final - tempo_inicial

    print(f"Tempo de execução: {tempo_total:.4f} segundos")
