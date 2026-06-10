import random
import time

def BubbleSort(arr):
    
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j] = temp
    return arr

tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

for tamanho in tamanhos:
    l = []
    for i in range(tamanho):
        l.append(random.randint(0, 1000))

    tempo_inicial = time.time()

    BubbleSort(l)

    tempo_final = time.time()

    tempo_total = tempo_final - tempo_inicial

    print(f"Tempo de execução: {tempo_total:.4f} segundos")
