from bubble_sort import BubbleSort
from bucket_sort import bucket_sort
from counting_sort import CountingSort
from heap_sort import heap_sort
from insertion_sort import insertionSort
from merge_sort import mergeSort
from quick_sort import quickSort
from radix_sort import radix_sort
from selection_sort import selectionSort
from shell_sort import shell_sort

import random as rd
import timeit
import matplotlib.pyplot as plt

l = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000] 

def fill_vector(n):
    arr = []
    for i in range(n):
        arr.append(rd.randint(1, 24000))
    return arr

timeBS = [] #Bubble
timeBkS = [] #Bucket
timeCS = [] #Couting
timeHS = [] #Heap
timeIS = [] #Insertion
timeMS = [] #Merge
timeQS = [] #Quick
timeRS = [] #Radix
timeSS = [] #Selection
timeShS = [] #Shell

for i in l:
    a = fill_vector(i)

    timeBS.append(timeit.timeit("BubbleSort({})".format(a.copy()), setup = "from __main__ import BubbleSort", number=1))
    timeBkS.append(timeit.timeit("bucket_sort({})".format(a.copy()), setup = "from __main__ import bucket_sort", number=1))
    timeCS.append(timeit.timeit("CountingSort({})".format(a.copy()), setup = "from __main__ import CountingSort", number=1))
    timeHS.append(timeit.timeit("heap_sort({})".format(a.copy()), setup = "from __main__ import heap_sort", number=1))
    timeIS.append(timeit.timeit("insertionSort({})".format(a.copy()), setup = "from __main__ import insertionSort", number=1))
    timeMS.append(timeit.timeit(lambda: mergeSort(a.copy(), 0, len(a)-1), number=1))
    timeQS.append(timeit.timeit(lambda: quickSort(a.copy(), 0, len(a)-1), number=1))
    timeRS.append(timeit.timeit("radix_sort({})".format(a.copy()), setup = "from __main__ import radix_sort", number=1))
    timeSS.append(timeit.timeit("selectionSort({})".format(a.copy()), setup = "from __main__ import selectionSort", number=1))
    timeShS.append(timeit.timeit("shell_sort({})".format(a.copy()), setup = "from __main__ import shell_sort", number=1))


fig, ax = plt.subplots()
ax.plot(l, timeBS, label="BubbleSort")
ax.plot(l, timeBkS, label="BucketSort")
ax.plot(l, timeCS, label="CountingSort")
ax.plot(l, timeHS, label="HeapSort")
ax.plot(l, timeIS, label="InsertionSort")
ax.plot(l, timeMS, label="MergeSort")
ax.plot(l, timeQS, label="QuickSort")
ax.plot(l, timeRS, label="RadixSort")
ax.plot(l, timeSS, label="SelectionSort")
ax.plot(l, timeShS, label="ShellSort")
ax.set_title("Comparison of Sorting Algorithms")
ax.set_xlabel("List size (elements)")
ax.set_ylabel("Time (seconds)")
ax.grid(True)
ax.legend()

plt.show()

#Considerando os algoritmos O(n²)
fig, ax = plt.subplots()

ax.plot(l, timeBS, label="BubbleSort")
ax.plot(l, timeIS, label="InsertionSort")
ax.plot(l, timeSS, label="SelectionSort")
ax.set_title("O(n²) Algorithms")
ax.set_xlabel("List size (elements)")
ax.set_ylabel("Time (seconds)")
ax.grid(True)
ax.legend()

plt.show()

#Considerando os algoritmos O(n log n)
fig, ax = plt.subplots()

ax.plot(l, timeMS, label="MergeSort")
ax.plot(l, timeQS, label="QuickSort")
ax.plot(l, timeHS, label="HeapSort")
ax.plot(l, timeShS, label="ShellSort")
ax.set_title("O(n log n) Algorithms")
ax.set_xlabel("List size (elements)")
ax.set_ylabel("Time (seconds)")
ax.grid(True)
ax.legend()

plt.show()

#Considerando os algoritmos lineares/especiais:
fig, ax = plt.subplots()

ax.plot(l, timeCS, label="CountingSort")
ax.plot(l, timeRS, label="RadixSort")
ax.plot(l, timeBkS, label="BucketSort")
ax.set_title("Linear and Special Cases")
ax.set_xlabel("List size (elements)")
ax.set_ylabel("Time (seconds)")
ax.grid(True)
ax.legend()

plt.show()

print("\n===== EXECUTION TIMES =====")

print(f"BubbleSort:    {timeBS}")
print(f"BucketSort:    {timeBkS}")
print(f"CountingSort:  {timeCS}")
print(f"HeapSort:      {timeHS}")
print(f"InsertionSort: {timeIS}")
print(f"MergeSort:     {timeMS}")
print(f"QuickSort:     {timeQS}")
print(f"RadixSort:     {timeRS}")
print(f"SelectionSort: {timeSS}")
print(f"ShellSort:     {timeShS}")
