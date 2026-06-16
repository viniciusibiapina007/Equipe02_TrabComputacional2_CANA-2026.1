#João Igor

def quickSort(arr, left, right):
    if left < right:
        i = partition(arr, left, right)
        quickSort(arr, left, i - 1)
        quickSort(arr, i + 1, right)
    return arr

def partition(arr, left, right):
    i = left

    for j in range(left + 1, right + 1):
        if arr[j] < arr[left]:
            i += 1
            swap(arr, i, j)

    swap(arr, left, i)

    return i

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
