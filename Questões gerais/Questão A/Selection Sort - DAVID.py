import random
import time

def selectionSort(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

for tamanho in tamanhos:
    l = []
    for i in range(tamanho):
        l.append(random.random())

    tempo_inicial = time.time()

    selectionSort(l)

    tempo_final = time.time()

    tempo_total = tempo_final - tempo_inicial

    print(f"Tempo de execução: {tempo_total:.4f} segundos")
