import matplotlib.pyplot as plt
import numpy as np
MULTCOUNT = 0
def inc():
    global MULTCOUNT
    MULTCOUNT = MULTCOUNT + 1

def zeroOut():
    global MULTCOUNT
    MULTCOUNT = 0

def decByOne(a,n):
    if n == 0:
        return 1
    if n > 0:
        inc()
        return a * decByOne(a, n-1)
    else:
        return -1

def decByCons(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        inc()
        temp = decByCons(a, n/2)
        return temp * temp
    else:
        inc()
        inc()
        temp = decByCons(a, (n-1)/2)
        return a * temp * temp

def divAndConq(a,n):
    if n == 0:
        return 1
    if n % 2 == 0:
        inc()
        return decByCons(a, n/2) * decByCons(a, n/2)
    else:
        inc()
        inc()
        return a * decByCons(a, (n-1)/2) * decByCons(a, (n-1)/2)

print("5 to the 6th using decrease by one = ", decByOne(5,6))
print("number of multiplications done by decrease by one: ", MULTCOUNT)
zeroOut()
print("5 to the 6th using decrease by constant = ", decByCons(5,6))
print("number of multiplications done by decrease by constant: ", MULTCOUNT)
zeroOut()
print("5 to the 6th using decrease by constant = ", divAndConq(5,6))
print("number of multiplications done by divide and conquer: ", MULTCOUNT)