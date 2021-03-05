#Preston Zimmerman
#Diana Arce
#Task Three 3/5/2021

import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from multiprocessing import Process, Queue
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
    count = 0
    for i in range(1, len(array)):
        for j in range(i-1, -1, -1):
            #inc('ins')
            count = count + 1
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            else:
                break
    return count

def selectionSort(array):
    count = 0
    for i in range(0, len(array)-1):
        smallest = i
        for j in range(i+1, len(array)):
            #inc('sel')
            count = count + 1
            if array[smallest] > array[j]:
                smallest = j
        temp = array[smallest]
        array[smallest] = array[i]
        array[i] = temp
    return count

def f(q, arrayToSort): #THIS HANDLES INSERTION SORT
    count = insertionSort(arrayToSort)
    q.put([count])

def e(q, arrayToSort): #THIS HANDLES SELECTION SORT
    count = selectionSort(arrayToSort)
    q.put([count])

if __name__ == '__main__':
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

        d1Count = insertionSort(dSetOne)
        d2Count = selectionSort(dSetTwo)

        print("Data set sorted using Insertion sort:")
        for q in range(0, len(dSetOne)):
            print(dSetOne[q], end=' ')
        print()
        print("Data set sorted using Selection sort:")
        for q in range(0, len(dSetOne)):
            print(dSetTwo[q], end=' ')
        print()

    elif mode == "scatter":
        if __name__ == '__main__':
            fname = 'data/testSet/data'
            xAxis = np.array(0)
            bestCaseInsYAxis = np.array(0)
            avgCaseInsYAxis = np.array(0)
            worstCaseInsYAxis = np.array(0)
            bestCaseSelYAxis = np.array(0)
            avgCaseSelYAxis = np.array(0)
            worstCaseSelYAxis = np.array(0)
            start = time.time()

            for x in range(200, 1600, 200):
                print("working on data", x)
                insSortSorted = np.loadtxt(fname + str(x) + '_sorted.txt', dtype=np.int64)  # sorted (best case)
                insSort = np.loadtxt(fname + str(x) + '.txt', dtype=np.int64)  # random data (avg case)
                insSortReverse = np.loadtxt(fname + str(x) + '_rSorted.txt', dtype=np.int64)  # reverse sorted (worst case)
                insSortSorted = insSortSorted.astype(int)
                insSort = insSort.astype(int)
                insSortReverse = insSortReverse.astype(int)
                selSortSorted = copy.deepcopy(insSortSorted)
                selSort = copy.deepcopy(insSort)
                selSortReverse = copy.deepcopy(insSortReverse)

                xAxis = np.append(xAxis, x)

                # This chunk generates the data for insertion sort on current file
                insSortSortedCount = insertionSort(insSortSorted)
                bestCaseInsYAxis = np.append(bestCaseInsYAxis, insSortSortedCount)
                insSortCount = insertionSort(insSort)
                avgCaseInsYAxis = np.append(avgCaseInsYAxis, insSortCount)
                insSortReverseCount = insertionSort(insSortReverse)
                worstCaseInsYAxis = np.append(worstCaseInsYAxis, insSortReverseCount)

                # This chunk generates the data for selection sort on current file
                selSortSortedCount = selectionSort(selSortSorted)
                bestCaseSelYAxis = np.append(bestCaseSelYAxis, selSortSortedCount)
                selSortCount = selectionSort(selSort)
                avgCaseSelYAxis = np.append(avgCaseSelYAxis, selSortCount)
                selSortReverseCount = selectionSort(selSortReverse)
                worstCaseSelYAxis = np.append(worstCaseSelYAxis, selSortReverseCount)

            for x in range(1600, 4200, 200):
                print("working on data", x)
                xAxis = np.append(xAxis, x)
                insSortSorted = np.loadtxt(fname + str(x) + '_sorted.txt', dtype=np.int64)  # sorted (best case)
                insSort = np.loadtxt(fname + str(x) + '.txt', dtype=np.int64)  # random data (avg case)
                insSortReverse = np.loadtxt(fname + str(x) + '_rSorted.txt', dtype=np.int64)  # reverse sorted (worst case)

                insSortSorted = insSortSorted.astype(int)
                insSort = insSort.astype(int)
                insSortReverse = insSortReverse.astype(int)
                selSortSorted = copy.deepcopy(insSortSorted)
                selSort = copy.deepcopy(insSort)
                selSortReverse = copy.deepcopy(insSortReverse)

                insertionBestQueue = Queue()
                p1 = Process(target=f, args=(insertionBestQueue, insSortSorted))
                insertionAvgQueue = Queue()
                p2= Process(target=f, args=(insertionAvgQueue, insSort))
                insertionWorstQueue = Queue()
                p3 = Process(target=f, args=(insertionWorstQueue, insSortReverse))
                selectionBestQueue = Queue()
                p4 = Process(target=e, args=(selectionBestQueue, selSortSorted))
                selectionAvgQueue = Queue()
                p5 = Process(target=e, args=(selectionAvgQueue, selSort))
                selectionWorstQueue = Queue()
                p6 = Process(target=e, args=(selectionWorstQueue, selSortReverse))
                p1.start()
                p2.start()
                p3.start()
                p4.start()
                p5.start()
                p6.start()
                bestCaseInsYAxis = np.append(bestCaseInsYAxis, insertionBestQueue.get())

                avgCaseInsYAxis = np.append(avgCaseInsYAxis, insertionAvgQueue.get())
                worstCaseInsYAxis = np.append(worstCaseInsYAxis, insertionWorstQueue.get())
                bestCaseSelYAxis = np.append(bestCaseSelYAxis, selectionBestQueue.get())
                avgCaseSelYAxis = np.append(avgCaseSelYAxis, selectionAvgQueue.get())
                worstCaseSelYAxis = np.append(worstCaseSelYAxis, selectionWorstQueue.get())
                p1.join()
                p2.join()
                p3.join()
                p4.join()
                p5.join()
                p6.join()
                #print(bestCaseInsYAxis)

            #OUTSIDE THAT BIG OL LOOOPIELOOP
            xAxis = np.delete(xAxis, 0)
            bestCaseInsYAxis = np.delete(bestCaseInsYAxis, 0)
            avgCaseInsYAxis = np.delete(avgCaseInsYAxis, 0)
            worstCaseInsYAxis = np.delete(worstCaseInsYAxis, 0)
            bestCaseSelYAxis = np.delete(bestCaseSelYAxis, 0)
            avgCaseSelYAxis = np.delete(avgCaseSelYAxis, 0)
            worstCaseSelYAxis = np.delete(worstCaseSelYAxis, 0)
            end = time.time()
            print("Time in seconds to generate data using threads: ", end - start)

            mpl.style.use('seaborn')
            #plt.rcParams['axes.facecolor'] = 'black'
            plt.xlim(0, np.amax(xAxis) + 100)
            plt.ylim(0, np.amax(bestCaseInsYAxis) * 1.1)
            #print(np.amax(bestCaseInsYAxis))
            ax = plt.gca()
            ax.get_xaxis().get_major_formatter().set_scientific(False)
            ax.get_yaxis().get_major_formatter().set_scientific(False)

            bestCaseInsPlot = plt.figure(1)
            plt.xlabel('Size of n')
            plt.ylabel('comparisons')
            plt.title('Best Case Insertion Sort')
            plt.scatter(xAxis, bestCaseInsYAxis, color="green", linewidth=1)

            avgCaseInsPlot = plt.figure(2)
            plt.xlim(0, np.amax(xAxis) + 100)
            plt.ylim(0, np.amax(worstCaseInsYAxis) * 1.1)
            ax = plt.gca()
            ax.get_xaxis().get_major_formatter().set_scientific(False)
            ax.get_yaxis().get_major_formatter().set_scientific(False)
            plt.xlabel('Size of n')
            plt.ylabel('comparisons')
            plt.title('Average Case Insertion Sort')
            plt.scatter(xAxis, avgCaseInsYAxis, color="yellow", linewidth=1)

            worstCaseInsPlot = plt.figure(3)
            plt.xlim(0, np.amax(xAxis) + 100)
            plt.ylim(0, np.amax(worstCaseInsYAxis) * 1.1)
            ax = plt.gca()
            ax.get_xaxis().get_major_formatter().set_scientific(False)
            ax.get_yaxis().get_major_formatter().set_scientific(False)
            plt.xlabel('Size of n')
            plt.ylabel('comparisons')
            plt.title('worst Case Insertion Sort')
            plt.scatter(xAxis, worstCaseInsYAxis, color="red", linewidth=1)

            bestCaseSelPlot = plt.figure(4)
            plt.xlim(0, np.amax(xAxis) + 100)
            plt.ylim(0, np.amax(bestCaseSelYAxis) * 1.1)
            ax = plt.gca()
            ax.get_xaxis().get_major_formatter().set_scientific(False)
            ax.get_yaxis().get_major_formatter().set_scientific(False)
            plt.xlabel('Size of n')
            plt.ylabel('comparisons')
            plt.title('Best Case Selection Sort')
            plt.scatter(xAxis, bestCaseSelYAxis, color="green", linewidth=1)

            avgCaseSelPlot = plt.figure(5)
            plt.xlim(0, np.amax(xAxis) + 100)
            plt.ylim(0, np.amax(avgCaseSelYAxis) * 1.1)
            ax = plt.gca()
            ax.get_xaxis().get_major_formatter().set_scientific(False)
            ax.get_yaxis().get_major_formatter().set_scientific(False)
            plt.xlabel('Size of n')
            plt.ylabel('comparisons')
            plt.title('Average Case Selection Sort')
            plt.scatter(xAxis, avgCaseSelYAxis, color="yellow", linewidth=1)

            worstCaseSelPlot = plt.figure(6)
            plt.xlim(0, np.amax(xAxis) + 100)
            plt.ylim(0, np.amax(worstCaseSelYAxis) * 1.1)
            ax = plt.gca()
            ax.get_xaxis().get_major_formatter().set_scientific(False)
            ax.get_yaxis().get_major_formatter().set_scientific(False)
            plt.xlabel('Size of n')
            plt.ylabel('comparisons')
            plt.title('Worst Case Selection Sort')
            plt.scatter(xAxis, worstCaseSelYAxis, color="red", linewidth=1)

            insAllThree = plt.figure(7)
            plt.xlim(0, np.amax(xAxis) + 100)
            plt.ylim(0, np.amax(worstCaseInsYAxis) * 1.1)
            ax = plt.gca()
            ax.get_xaxis().get_major_formatter().set_scientific(False)
            ax.get_yaxis().get_major_formatter().set_scientific(False)
            plt.xlabel('Size of n')
            plt.ylabel('comparisons')
            plt.title('All three Insertion sort cases')
            plt.plot(xAxis, bestCaseInsYAxis, '.g-' ,color="green", linewidth=1, label="best case")
            plt.plot(xAxis, avgCaseInsYAxis, '.y-' ,color="yellow", linewidth=1, label="avg case")
            plt.plot(xAxis, worstCaseInsYAxis, '.r-' ,color="red", linewidth=1, label="worst case")
            plt.legend(loc="upper left")

            plt.show()

    else:
        print("please run program again and enter a valid mode with no ' ' around it")

