import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import logging
import threading
import time

INSCOUNT = 0
SELCOUNT = 0

def inc(name):
    if name == "ins":
        global INSCOUNT
        INSCOUNT = INSCOUNT + 1
    if name == 'sel':
        global SELCOUNT
        SELCOUNT = SELCOUNT + 1

def zeroOut(name):
    if name == "ins":
        global INSCOUNT
        INSCOUNT = 0
    if name == 'sel':
        global SELCOUNT
        SELCOUNT = 0

def insertionSort(array):
    for i in range(1, len(array)):
        for j in range(i-1, -1, -1):
            inc('ins')
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            else:
                break
    return array

def selectionSort(array):
    for i in range(0, len(array)-1):
        smallest = i
        for j in range(i+1, len(array)):
            inc('sel')
            if array[smallest] > array[j]:
                smallest = j
        temp = array[smallest]
        array[smallest] = array[i]
        array[i] = temp
    return array

fname = 'data/testSet/data'

xAxis = np.array(0)
bestCaseInsYAxis = np.array(0)
avgCaseInsYAxis = np.array(0)
worstCaseInsYAxis = np.array(0)
bestCaseSelYAxis = np.array(0)
avgCaseSelYAxis = np.array(0)
worstCaseSelYAxis = np.array(0)

for x in range(100, 6000, 500):
    print("working on data", x)
    insSortSorted = np.loadtxt(fname + str(x) + '_sorted.txt', dtype=np.int64)  # sorted (best case)
    insSort = np.loadtxt(fname + str(x) + '.txt', dtype = np.int64) #random data (avg case)
    insSortReverse = np.loadtxt(fname + str(x) + '_rSorted.txt', dtype = np.int64) #reverse sorted (worst case)

    insSortSorted = insSortSorted.astype(int)
    insSort = insSort.astype(int)
    insSortReverse = insSortReverse.astype(int)
    selSortSorted = copy.deepcopy(insSortSorted)
    selSort = copy.deepcopy(insSort)
    selSortReverse = copy.deepcopy(insSortReverse)

    #This chunk generates the data for insertion sort on current file
    insSortSorted = insertionSort(insSortSorted)
    xAxis = np.append(xAxis, x)
    bestCaseInsYAxis = np.append(bestCaseInsYAxis, INSCOUNT)
    print("x: ", x, " num comps for best: ", INSCOUNT)
    zeroOut('ins')
    insSort = insertionSort(insSort)
    avgCaseInsYAxis = np.append(avgCaseInsYAxis, INSCOUNT)
    print("x: ", x, " num comps for avg: ", INSCOUNT)
    zeroOut('ins')
    insSortReverse = insertionSort(insSortReverse)
    worstCaseInsYAxis = np.append(worstCaseInsYAxis, INSCOUNT)
    print("x: ", x, " num comps for worst: ", INSCOUNT)
    zeroOut('ins')

    #This chunk generates the data for selection sort on current file
    selSortSorted = selectionSort(selSortSorted)
    bestCaseSelYAxis = np.append(bestCaseSelYAxis, SELCOUNT)
    print("x: ", x, " num comps for best: ", SELCOUNT)
    zeroOut('sel')
    selSort = selectionSort(selSort)
    avgCaseSelYAxis = np.append(avgCaseSelYAxis, SELCOUNT)
    print("x: ", x, " num comps for avg: ", SELCOUNT)
    zeroOut('sel')
    selSortReverse = selectionSort(selSortReverse)
    worstCaseSelYAxis = np.append(worstCaseSelYAxis, SELCOUNT)
    print("x: ", x, " num comps for worst: ", SELCOUNT)
    zeroOut('sel')

xAxis = np.delete(xAxis, 0)
bestCaseInsYAxis = np.delete(bestCaseInsYAxis, 0)
avgCaseInsYAxis = np.delete(avgCaseInsYAxis, 0)
worstCaseInsYAxis = np.delete(worstCaseInsYAxis,0)
bestCaseSelYAxis = np.delete(bestCaseSelYAxis, 0)
avgCaseSelYAxis = np.delete(avgCaseSelYAxis, 0)
worstCaseSelYAxis = np.delete(worstCaseSelYAxis, 0)

mpl.style.use('seaborn')
plt.xlim(0, 6000)
plt.ylim(0, np.amax(bestCaseInsYAxis))
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_scientific(False)

bestCaseInsPlot = plt.figure(1)
plt.xlabel('Size of n')
plt.ylabel('comparisons')
plt.title('Best Case Insertion Sort')
plt.plot(xAxis, bestCaseInsYAxis, color="green", linewidth=1)

avgCaseInsPlot = plt.figure(2)
plt.xlim(0, 6000)
plt.ylim(0, np.amax(worstCaseInsYAxis))
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_scientific(False)
plt.xlabel('Size of n')
plt.ylabel('comparisons')
plt.title('Average Case Insertion Sort')
plt.plot(xAxis, avgCaseInsYAxis, color="yellow", linewidth=1)

avgCaseInsPlot = plt.figure(3)
plt.xlim(0, 6000)
plt.ylim(0, np.amax(worstCaseInsYAxis))
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_scientific(False)
plt.xlabel('Size of n')
plt.ylabel('comparisons')
plt.title('worst Case Insertion Sort')
plt.plot(xAxis, worstCaseInsYAxis, color="red", linewidth=1)

bestCaseSelPlot = plt.figure(4)
plt.xlim(0, 6000)
plt.ylim(0, np.amax(bestCaseSelYAxis))
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_scientific(False)
plt.xlabel('Size of n')
plt.ylabel('comparisons')
plt.title('Best Case Selection Sort')
plt.plot(xAxis, bestCaseSelYAxis, color="green", linewidth=1)

avgCaseSelPlot = plt.figure(5)
plt.xlim(0, 6000)
plt.ylim(0, np.amax(avgCaseSelYAxis))
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_scientific(False)
plt.xlabel('Size of n')
plt.ylabel('comparisons')
plt.title('Average Case Selection Sort')
plt.plot(xAxis, avgCaseSelYAxis, color="yellow", linewidth=1)

worstCaseSelPlot = plt.figure(6)
plt.xlim(0, 6000)
plt.ylim(0, np.amax(worstCaseSelYAxis))
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_scientific(False)
plt.xlabel('Size of n')
plt.ylabel('comparisons')
plt.title('Worst Case Selection Sort')
plt.plot(xAxis, worstCaseSelYAxis, color="red", linewidth=1)

plt.show()


