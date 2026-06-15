import random as rd

t = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

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

def preencherArr(arr, n):
    for i in range(n):
        arr.append(rd.randint(0, 25000))
    return arr

def main(): #corrijir apenas impressão
    op = int(input("1- 1000\n2- 3000\n3- 6000\n4- 9000\n5- 12000\n6- 15000\n7- 18000\n8- 21000\n9- 24000\n10- teste\n0- sair\nInforme uma opção de tamanho: "))

    while op != 0:

        if op == 1:
            n = t[0]

        elif op == 2:
            n = t[1]

        elif op == 3:
            n = t[2]

        elif op == 4:
            n = t[3]

        elif op == 5:
            n = t[4]

        elif op == 6:
            n = t[5]

        elif op == 7:
            n = t[6]

        elif op == 8:
            n = t[7]

        elif op == 9:
            n = t[8]

        elif op == 10:
            n = 10

        else:
            n = 0

        if n > 0:
            arr = []
            arr = preencherArr(arr, n)
            quickSort(arr, 0, n - 1)
            print(arr)

        op = int(input("1- 1000\n2- 3000\n3- 6000\n4- 9000\n5- 12000\n6- 15000\n7- 18000\n8- 21000\n9- 24000\n10- teste\n0- sair\nInforme uma opção de tamanho: "))

main()
