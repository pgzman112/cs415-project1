#Preston Zimmerman
#Diana Arce
#Task Three 3/5/2021

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
        INSCOUNT = 1
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

#def selTwoSort(array, count):
#    for i in range(0, len(array)-1):
#        smallest = i
#        for j in range(i+1, len(array)):
#            count = count + 1
#            if array[smallest] > array[j]:
#                smallest = j
#        temp = array[smallest]
#        array[smallest] = array[i]
#        array[i] = temp
#     return count


mode = input("Enter 'test' for test mode and 'scatter' for scatter plot mode: ")
if mode == "test":
    value = input("Please enter a size of list n between 10 and 100 with increments of 10: ")
    value = int(value)
    if value % 10 != 0 or value < 10 or value > 100:
        print("input value was not between 10 and 100 or in increments of 10 please rerun program and try again")
        exit(-1)
    fname = 'data/smallSet/data'
    dSetOne = np.loadtxt(fname + str(value) + '.txt', dtype=np.int64)
    dSetTwo = np.loadtxt(fname + str(value) + '.txt', dtype=np.int64)

    print("Data before sorting:")
    for q in range(0, len(dSetOne)):
        print(dSetOne[q], end=' ')
    print()

    dSetOne = insertionSort(dSetOne)
    dSetTwo = insertionSort(dSetTwo)

    print("Data set sorted using Insertion sort:")
    for q in range(0, len(dSetOne)):
        print(dSetOne[q], end=' ')
    print()
    print("Data set sorted using Selection sort:")
    for q in range(0, len(dSetOne)):
        print(dSetTwo[q], end=' ')
    print()

elif mode == "scatter":

    fname = 'data/testSet/data'

    xAxis = np.array(0)
    bestCaseInsYAxis = np.array(0)
    avgCaseInsYAxis = np.array(0)
    worstCaseInsYAxis = np.array(0)
    bestCaseSelYAxis = np.array(0)
    avgCaseSelYAxis = np.array(0)
    worstCaseSelYAxis = np.array(0)

    for x in range(100, 4000, 200):
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
    plt.xlim(0, np.amax(xAxis) + 100)
    plt.ylim(0, np.amax(bestCaseInsYAxis)* 1.1)
    print(np.amax(bestCaseInsYAxis))
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_scientific(False)

    bestCaseInsPlot = plt.figure(1)
    plt.xlabel('Size of n')
    plt.ylabel('comparisons')
    plt.title('Best Case Insertion Sort')
    plt.scatter(xAxis, bestCaseInsYAxis, color="green", linewidth=1)

    avgCaseInsPlot = plt.figure(2)
    plt.xlim(0, np.amax(xAxis) + 100)
    plt.ylim(0, np.amax(worstCaseInsYAxis)* 1.1)
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    plt.xlabel('Size of n')
    plt.ylabel('comparisons')
    plt.title('Average Case Insertion Sort')
    plt.scatter(xAxis, avgCaseInsYAxis, color="yellow", linewidth=1)

    avgCaseInsPlot = plt.figure(3)
    plt.xlim(0, np.amax(xAxis) + 100)
    plt.ylim(0, np.amax(worstCaseInsYAxis) * 1.1)
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    plt.xlabel('Size of n')
    plt.ylabel('comparisons')
    plt.title('worst Case Insertion Sort')
    plt.scatter(xAxis, worstCaseInsYAxis, color="red", linewidth=1)

    bestCaseSelPlot = plt.figure(4)
    plt.xlim(0, np.amax(xAxis) + 100)
    plt.ylim(0, np.amax(bestCaseSelYAxis)* 1.1)
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    plt.xlabel('Size of n')
    plt.ylabel('comparisons')
    plt.title('Best Case Selection Sort')
    plt.scatter(xAxis, bestCaseSelYAxis, color="green", linewidth=1)

    avgCaseSelPlot = plt.figure(5)
    plt.xlim(0, np.amax(xAxis) + 100)
    plt.ylim(0, np.amax(avgCaseSelYAxis)* 1.1)
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    plt.xlabel('Size of n')
    plt.ylabel('comparisons')
    plt.title('Average Case Selection Sort')
    plt.scatter(xAxis, avgCaseSelYAxis, color="yellow", linewidth=1)

    worstCaseSelPlot = plt.figure(6)
    plt.xlim(0, np.amax(xAxis) + 100)
    plt.ylim(0, np.amax(worstCaseSelYAxis)* 1.1)
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    plt.xlabel('Size of n')
    plt.ylabel('comparisons')
    plt.title('Worst Case Selection Sort')
    plt.scatter(xAxis, worstCaseSelYAxis, color="red", linewidth=1)

    insAllThree = plt.figure(7)
    plt.xlim(0, np.amax(xAxis) + 100)
    plt.ylim(0, np.amax(worstCaseInsYAxis)* 1.1)
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    plt.xlabel('Size of n')
    plt.ylabel('comparisons')
    plt.title('All three Insertion sort cases')
    plt.plot(xAxis, bestCaseInsYAxis, color="green", linewidth=1, label="best case")
    plt.plot(xAxis, avgCaseInsYAxis, color="yellow", linewidth=1, label="avg case")
    plt.plot(xAxis, worstCaseInsYAxis, color="red", linewidth=1, label="worst case")
    plt.legend(loc = "upper left")

    plt.show()

else:
    print("please run program again and enter a valid mode with no ' ' around it")