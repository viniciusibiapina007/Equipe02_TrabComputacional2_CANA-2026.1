import random
import timeit

def bucket_sort(lista):
    if len(lista) == 0:
        return lista

    # Encontrar valores mínimo e máximo
    menor = min(lista)
    maior = max(lista)

    # Criar os baldes
    quantidade_baldes = len(lista)
    baldes = [[] for _ in range(quantidade_baldes)]

    # Distribuir os elementos nos baldes
    for valor in lista:
        indice = int((valor - menor) * (quantidade_baldes - 1) / (maior - menor)) if maior != menor else 0
        baldes[indice].append(valor)

    # Ordenar cada balde e juntar os resultados
    resultado = []
    for balde in baldes:
        resultado.extend(sorted(balde))

    return resultado



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

