import random as rd

t = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]

def mergeSort(arr, p, r):
      if p < r:
          q = (p + r) // 2
          mergeSort(arr, p, q)
          mergeSort(arr, q + 1, r)
          merge(arr, p, q, r)
      return arr

def merge(arr, p, q, r):
      n1 = q - p + 1
      n2 = r - q

      L = [0] * n1
      R = [0] * n2

      for i in range(n1):
          L[i] = arr[p + i]

      for j in range(n2):
          R[j] = arr[q + 1 + j]

      i = 0
      j = 0
      k = p

      while i < n1 and j < n2:
          if L[i] <= R[j]:
              arr[k] = L[i]
              i += 1
          else:
              arr[k] = R[j]
              j += 1
          k += 1

      while i < n1:
          arr[k] = L[i]
          i += 1
          k += 1

      while j < n2:
          arr[k] = R[j]
          j += 1
          k += 1

def preencherArr(arr, n):
      for i in range(n):
          arr.append(rd.randint(0, 25000))
      return arr

def main():
    op = int(input("1- 1000\n2- 3000\n3- 6000\n4- 9000\n5- 12000\n6- 15000\n7- 18000\n8- 21000\n9- 24000\n10- teste\n0- sair\nInforme uma opção de tamanho: ")) #OBS: apenas implementar melhor visão de que a ordenação foi feita

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
            mergeSort(arr, 0, n - 1)
            print(arr)

        op = int(input("1- 1000\n2- 3000\n3- 6000\n4- 9000\n5- 12000\n6- 15000\n7- 18000\n8- 21000\n9- 24000\n10- teste\n0- sair\nInforme uma opção de tamanho: "))

main()
