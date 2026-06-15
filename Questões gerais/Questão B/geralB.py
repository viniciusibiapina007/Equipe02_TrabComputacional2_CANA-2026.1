import matplotlib.pyplot as plt
import random
import timeit


def CountingSort(arr):
    n = len(arr)

    max_valor = max(arr)  # pega o maior elemento do array

    count = [0] * (max_valor + 1)  # cria o array de contagem com o tamanho do maior elemento + 1
    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):  # percorre o array de contagem e soma o valor dos elementos
        count[i] += count[i - 1]

    saida = [0] * len(arr)  # cria o array de saida com o valor de entrada
    for i in range(len(arr) - 1, -1, -1):  # vai ser implementado de tras para frente para manter estabiliadade
        num = arr[i]
        index = count[num] - 1
        saida[index] = num
        count[num] -= 1

    return saida
# ===============================================================================================


def geraLista(tam):
    random.seed()
    i = 0
    lista = []
    while i < tam:
        lista.append(random.randint(1, tam))
        i += 1

    return lista

# ===============================================================================================


def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  # Retorna a posição onde encontrou
    return -1  # Retorna -1 se não encontrar


def busca_linear_sentinela(lista, valor):
    n = len(lista)

    # Guarda o último elemento
    ultimo = lista[n - 1]

    # Coloca a sentinela
    lista[n - 1] = valor

    i = 0
    while lista[i] != valor:
        i += 1

    # Restaura o último elemento
    lista[n - 1] = ultimo

    # Verifica se encontrou de verdade
    if i < n - 1 or ultimo == valor:
        return i
    else:
        return -1


def busca_binaria(array, valor):
    lista = CountingSort(array)
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def busca_binaria_rapida(array, alvo):
    lista = CountingSort(array)
    baixo = 0
    alto = len(lista) - 1

    while baixo < alto:
        meio = (baixo + alto) // 2
        # Apenas uma comparação por passo
        if lista[meio] < alvo:
            baixo = meio + 1
        else:
            alto = meio

    # Verifica se o elemento encontrado é o alvo
    if lista[baixo] == alvo:
        return baixo
    return -1

# ====================================================================================

tamanhos = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
temposBLinearConv = []
temposBLinearSent = []
temposBBinariaConv = []
temposBBinariaRapd = []

for t in tamanhos:
    lista = geraLista(t)
    n = random.randint(1,t)
    temposBLinearConv.append(timeit.timeit(f'busca_linear({lista.copy()}, {n})', setup='from __main__ import busca_linear', number=1))
    temposBLinearSent.append(timeit.timeit(f'busca_linear_sentinela({lista.copy()}, {n})', setup='from __main__ import busca_linear_sentinela', number=1))
    temposBBinariaConv.append(timeit.timeit(f'busca_binaria({lista.copy()}, {n})', setup='from __main__ import busca_binaria', number=1))
    temposBBinariaRapd.append(timeit.timeit(f'busca_binaria_rapida({lista.copy()}, {n})', setup='from __main__ import busca_binaria_rapida', number=1))


print(temposBLinearConv)
print(temposBLinearSent)
print(temposBBinariaConv)
print(temposBBinariaRapd)

plt.figure(figsize=(10, 6))

plt.plot(tamanhos, temposBLinearConv, label='busca_linear')
plt.plot(tamanhos, temposBLinearSent, label='busca_linear_sentinela')
plt.plot(tamanhos, temposBBinariaConv, label='busca_binaria')
plt.plot(tamanhos, temposBBinariaRapd, label='busca_binaria_rapida')

plt.title('Comparativo entre o tempo de execução das buscas')
plt.xlabel('Tamanho do vetor')
plt.ylabel('Tempo de execução (s)')

plt.grid(True)
plt.legend()

plt.show()
