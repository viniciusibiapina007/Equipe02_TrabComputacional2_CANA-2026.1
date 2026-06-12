import random
import timeit

def shell_sort(lista):
    n = len(lista)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i

            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap

            lista[j] = temp

        gap //= 2

    return lista


def geraLista(tam):
    random.seed()
    i = 0
    lista = []
    while i < tam:
        lista.append(random.randint(1, tam))
        i += 1

    return lista


tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

for t in tamanhos:
    lista = geraLista(t)
    print(sum(lista))
