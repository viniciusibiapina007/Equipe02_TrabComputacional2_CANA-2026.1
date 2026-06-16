#David Lucas

def insertionSort(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i -1
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual
        
    return lista
