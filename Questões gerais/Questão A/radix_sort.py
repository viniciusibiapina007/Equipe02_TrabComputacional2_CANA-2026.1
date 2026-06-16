# José Gabriel

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
