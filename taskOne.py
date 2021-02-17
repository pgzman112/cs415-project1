import matplotlib.pyplot as plt
import numpy as np
import logging
import threading
import time

FIBCOUNTER = 0
GCDCOUNTER = 0
def increment(name):
    if name == fib:
        global FIBCOUNTER
        FIBCOUNTER = FIBCOUNTER + 1
    if name == gcd:
        global GCDCOUNTER
        GCDCOUNTER = GCDCOUNTER + 1

def zeroOut(name):
    if name == fib:
        global FIBCOUNTER
        FIBCOUNTER = 0

def fib(k):
    if k == 0:
        return 0
    if k == 1:
        increment(fib)
        return 1
    else:
        return fib(k-1) + fib(k-2)

def gcd(m, n):
    if m == 0 or n == 0:
        return -1
    if m % n == 0:
        return n
    else:
        increment(gcd)
        return gcd(n, m % n)

mode = input("Enter 'test' for test mode and 'scatter' for scatter plot mode: ")
if mode == "test":
    value = input("Enter kth term: ")
    value = int(value)
    print("The kth value of fib is: ", fib(value))
    print("num of additions made: ", FIBCOUNTER)
    mm = fib(value+1)
    nn = fib(value)
    print("fib of k+1: ", mm)
    print("fib of k: ", nn)
    print("The gcd of your k+1 and k: ", gcd(mm, nn))
    print("num of divs made: ", GCDCOUNTER)
elif mode == "scatter":
    print("Do some stuff")
    xAxis = np.array(12)
    yAxis = np.array(12)
    for i in range (1,30):
        xAxis = np.append(xAxis, i)
        temp = fib(i)
        yAxis = np.append(yAxis, FIBCOUNTER)
        zeroOut(fib)
    print(xAxis)
    print(yAxis)
    plt.scatter(xAxis, yAxis)
    plt.show()
    print("did we finish?")

elif mode == "display":
    for i in range(0,13):
        print(fib(i))
else:
    print("incorrect input please run the program and try again")
