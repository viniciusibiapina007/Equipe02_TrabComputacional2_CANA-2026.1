#José Gabriel

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
