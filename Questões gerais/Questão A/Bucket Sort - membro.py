import random
import timeit

def insertion_sort(bld):
    """Ordena cada balde individualmente."""
    for i in range(1, len(bld)):
        key = bld[i]
        j = i - 1
        while j >= 0 and bld[j] > key:
            bld[j + 1] = bld[j]
            j -= 1
        bld[j + 1] = key
    return bld


def bucket_sort(arr):
    if not arr:
        return arr

    # 1. Criação dos baldes ========================================
    qtd_balde = len(arr)
    max_val = max(arr)
    min_val = min(arr)

    # Range de valores por balde
    faixa_balde = (max_val - min_val) / qtd_balde + 1

    baldes = [[] for _ in range(qtd_balde)]

    # 2. Distribuição dos elementos nos baldes ======================
    for num in arr:
        index = int((num - min_val) / faixa_balde)
        baldes[index].append(num)

    # 3. Ordenação de cada balde e concatenação ======================
    array_ordenado = []
    for balde in baldes:
        array_ordenado.extend(insertion_sort(balde))

    return array_ordenado


def geraLista(tam):
    random.seed()
    i = 0
    lista = []
    while i < tam:
        lista.append(random.randint(1, tam))
        i += 1

    return lista


tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
tempos = []

for t in tamanhos:
    lista = geraLista(t)
    tempos.append(timeit.timeit(f'bucket_sort({lista.copy()})', setup='from __main__ import bucket_sort', number=1))

    print(sum(lista))

print(tempos)
