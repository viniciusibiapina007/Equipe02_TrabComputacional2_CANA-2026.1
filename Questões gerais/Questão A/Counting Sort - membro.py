import random
import time

def CountingSort(arr):

    n = len(arr)
    
    max_valor = max(arr) # pega o maior elemento do array 

    count = [0] * (max_valor + 1) # cria o array de contagem com o tamanho do maior elemento + 1 
    for num in arr:
        count[num] += 1
    
    for i in range(1, len(count)): # percorre o array de contagem e soma o valor dos elementos
        count[i] += count[i - 1]

    saida = [0] * len(arr) # cria o array de saida com o valor de entrada
    for i in range(len(arr) - 1, -1, -1): # vai ser implementado de tras para frente para manter estabiliadade
        num = arr[i]
        index = count[num] - 1
        saida[index] = num
        count[num] -= 1

    return saida


tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

for tamanho in tamanhos:
    l = []
    for i in range(tamanho):
        l.append(random.randint(0, 1000))

    tempo_inicial = time.time()

    CountingSort(l)

    tempo_final = time.time()

    tempo_total = tempo_final - tempo_inicial

    print(f"Tempo de execução: {tempo_total:.4f} segundos")
