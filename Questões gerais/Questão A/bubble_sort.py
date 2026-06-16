import random #João Arthur
import time

def BubbleSort(arr):
    
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j] = temp
    return arr
