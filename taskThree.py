import copy
import numpy as np

def insertionSort(array):
    start = 0
    while start < len(array):
        for i in range(start, 0, -1):
            if array[i] < array[i-1]:
                temp = array[i]
                array[i] = array[i-1]
                array[i-1] = temp
        start = start + 1
    return array

def selectionSort(array):
    for i in range(0, len(array)-1):
        smallest = i
        for j in range(i+1, len(array)):
            if array[smallest] > array[j]:
                smallest = j
        temp = array[smallest]
        array[smallest] = array[i]
        array[i] = temp
    return array

fname = 'data/smallSet/data'
n = 20
#adding a comment
temp = np.loadtxt(fname + str(n) + '.txt', dtype = np.int64)

temp = temp.astype(int)
temp1 = copy.deepcopy(temp)
print("array unsorted: ")
for i in temp:
    print(i, end = ' ')

print()
print("sorted array using insertion sort: ")
t = insertionSort(temp)
for i in t:
    print(i, end = ' ')

print()

print("array unsorted: ")
for i in temp1:
    print(i, end = ' ')
print()
print("sorted array using selection sort: ")
y = selectionSort(temp1)
for i in y:
    print(i, end = ' ')
