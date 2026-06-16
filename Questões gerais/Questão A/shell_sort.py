#Vinicius Rolim

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
