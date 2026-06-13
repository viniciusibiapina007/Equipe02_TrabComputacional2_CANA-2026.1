class Funcionário:
   def __init__(self, nome, salario):
      self.__nome = nome
      self.__salario = salario

   def obterNome(self):
       return self.__nome

   def alterarNome(self, nome):
      self.__nome = nome

   def obterSalario(self):
      return self.__salario

   def alterarSalario(self, salario):
       self.__salario = salario

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
          if L[i].obterSalario() <= R[j].obterSalario():
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

def quickSort(arr, left, right):
   if left < right:
      i = partition(arr, left, right)
      quickSort(arr, left, i - 1)
      quickSort(arr, i + 1, right)
   return arr

def partition(arr, left, right):
   i = left

   for j in range(left + 1, right + 1):
      if arr[j].obterNome() < arr[left].obterNome():
         i += 1
         swap(arr, i, j)

   swap(arr, left, i)

   return i

def swap(arr, a, b):
   temp = arr[a]
   arr[a] = arr[b]
   arr[b] = temp

func1 = Funcionário("Dondon", 10000)
func2 = Funcionário("João", 1)
func3 = Funcionário("José", 30)
func4 = Funcionário("David", 700)
func5 = Funcionário("Vinícius", 500)

lista = [func1, func2, func3, func4, func5]

def main():
   print("Lista de funcionários:")
   for i in range(len(lista)):
      print(f"{lista[i].obterNome()} - {lista[i].obterSalario()}")

   op = int(input("\n1- Ordenar por salário (Merge Sort)\n2- Ordenar por nome (Quick Sort)\nEscolha uma opção de ordenação: "))

   if op == 1:
      mergeSort(lista, 0, len(lista) - 1)

      print("\nLista ordenada por salário:")
      for i in range(len(lista)):
         print(f"{lista[i].obterNome()} - {lista[i].obterSalario()}")

   elif op == 2:
      quickSort(lista, 0, len(lista) - 1)

      print("\nLista ordenada por nome:")
      for i in range(len(lista)):
         print(f"{lista[i].obterNome()} - {lista[i].obterSalario()}")

   else:
      print("Opção inválida.")

main()
