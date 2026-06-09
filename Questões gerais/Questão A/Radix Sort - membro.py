# José Gabriel
import random
import time

def counting_sort(vetor, exp):
    n = len(vetor)
    saida = [0] * n
    contagem = [0] * 10

    for numero in vetor:
        indice = (numero // exp) % 10
        contagem[indice] += 1

    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    for i in range(n - 1, -1, -1):
        indice = (vetor[i] // exp) % 10
        saida[contagem[indice] - 1] = vetor[i]
        contagem[indice] -= 1

    for i in range(n):
        vetor[i] = saida[i]

def radix_sort(vetor):
    if len(vetor) == 0:
        return vetor
        
    maior = max(vetor)
    exp = 1
    while maior // exp > 0:
        counting_sort(vetor, exp)
        exp *= 10
    return vetor

tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
tempos = []
arr = None

for n in tamanhos:
    vetor = [random.randint(0, 24000) for _ in range(n)]

    inicio = time.perf_counter()
    radix_sort(vetor)
    fim = time.perf_counter()

    tempos.append(fim - inicio)
    arr = vetor

print(tempos)
print("RESULTADO DA ORDENAÇÃO (Último Teste)")
print(f"Tamanho do vetor : {len(arr)}")
print(f"Menor elemento   : {arr[0]}")
print(f"Maior elemento   : {arr[-1]}")
print(f"Primeiros 10     : {arr[:10]}")
print(f"Últimos 10       : {arr[-10:]}")  