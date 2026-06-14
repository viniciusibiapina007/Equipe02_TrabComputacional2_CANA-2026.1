import matplotlib.pyplot as plt
import random
import timeit


def shell_sort(arr):
    n = len(arr)
    meio = n // 2

    while meio > 0:
        for i in range(meio, n):
            temp = arr[i]
            j = i

            while j >= meio and arr[j - meio] > temp:
                arr[j] = arr[j - meio]
                j -= meio

            arr[j] = temp

        meio //= 2

    return arr


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
    tempos.append(timeit.timeit(f'shell_sort({lista.copy()})', setup='from __main__ import shell_sort', number=1))
