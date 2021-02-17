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
        return decByCons(a, n/2) * decByCons(a, n/2)
    else:
        inc()
        inc()
        return a * decByCons(a, (n-1)/2) * decByCons(a, (n-1)/2)

def divAndConq(a,n):
    if a == 0:
        return 0
    elif n == 0:
        return 1
    elif n < 0:
        return 0
    elif n < 1:
        return 1
    elif n % 2 == 0:
        inc()
        return divAndConq(a*a, n/2)
    else:
        inc()
        inc()
        return a * divAndConq(a*a, n/2)

print("3 squared using decrease by one = ", decByOne(5,3))
print("number of multiplications done by decrease by one: ", MULTCOUNT)
zeroOut()
print("3 squared using decrease by constant = ", decByCons(5,3))
print("number of multiplications done by decrease by constant: ", MULTCOUNT)
zeroOut()
print("3 squared using decrease by constant = ", divAndConq(5,3))
print("number of multiplications done by divide and conquer: ", MULTCOUNT)