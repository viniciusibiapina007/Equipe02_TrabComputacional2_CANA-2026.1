import random
import time

def heapify(vetor, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n and vetor[esq] > vetor[maior]:
        maior = esq

    if dir < n and vetor[dir] > vetor[maior]:
        maior = dir

    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]
        heapify(vetor, n, maior)

def heap_sort(vetor):
    n = len(vetor)
    for i in range(n // 2 - 1, -1, -1):
        heapify(vetor, n, i)
    for i in range(n - 1, 0, -1):
        vetor[0], vetor[i] = vetor[i], vetor[0]
        heapify(vetor, i, 0)
    return vetor

tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
tempos = []
arr = None

for n in tamanhos:
    vetor = [random.randint(0, 24000) for _ in range(n)]
    
    inicio = time.perf_counter()
    heap_sort(vetor)
    fim = time.perf_counter()
    
    tempos.append(fim - inicio)
    arr = vetor

print(tempos)
print("RESULTADO DA ORDENAÇÃO (Último Teste)")
print("="*40)
print(f"Tamanho do vetor : {len(arr)}")
print(f"Menor elemento   : {arr[0]}")
print(f"Maior elemento   : {arr[-1]}")
print(f"Primeiros 10     : {arr[:10]}")
print(f"Últimos 10       : {arr[-10:]}")
 