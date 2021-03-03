#Preston Zimmerman
#Diana Arce
#Task Two 3/5/2021
import matplotlib.pyplot as plt
import matplotlib as mpl
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
        return divAndConq(a, n/2) * divAndConq(a, n/2)
    else:
        inc()
        inc()
        return a * divAndConq(a, (n-1)/2) * divAndConq(a, (n-1)/2)

mode = input("Enter 'test' for test mode and 'scatter' for scatter plot mode: ")
if mode == "test":
    #do stuff
    a = input("Please enter a value for the constant 'a' ")
    n = input("Please enter a value n to calculate 'a^n'")
    a = int(a)
    n = int(n)

    print(a, " raised to the power of ", n, " using decrease by one algorithm: ", decByOne(a,n))
    print("Decrease By one did: ", MULTCOUNT, " multiplications")
    zeroOut()
    print(a, " raised to the power of ", n, " using decrease by constant factor algorithm: ", decByCons(a,n))
    print("Decrease By Constant did: ", MULTCOUNT, " multiplications")
    zeroOut()
    print(a, " raised to the power of ", n, " using divide and conquer algorithm: ", divAndConq(a, n))
    print("Divide and conquer did: ", MULTCOUNT, " multiplications")
    zeroOut()

elif mode == "scatter":
    #do stuff
    a = 5
    xAxis = np.array(0)
    decByOneMults = np.array(0)
    decByConsMults = np.array(0)
    divAndConqMults = np.array(0)
    for i in range(0, 100):
        xAxis = np.append(xAxis, i)
        decByOne(a, i)
        decByOneMults = np.append(decByOneMults, MULTCOUNT)
        zeroOut()
        decByCons(a, i)
        decByConsMults = np.append(decByConsMults, MULTCOUNT)
        zeroOut()
        divAndConq(a, i)
        divAndConqMults = np.append(divAndConqMults, MULTCOUNT)
        zeroOut()

    decByOneMults = np.delete(decByOneMults, 0)
    xAxis = np.delete(xAxis, 0)
    decByConsMults = np.delete(decByConsMults, 0)
    divAndConqMults = np.delete(divAndConqMults, 0)

    mpl.style.use('seaborn')
    plt.xlim(0, 105)
    plt.ylim(0, np.amax(divAndConqMults) + 25)
    ax = plt.gca()
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    ax.get_yaxis().get_major_formatter().set_scientific(False)


    plotPlot = plt.figure(1)
    plt.xlabel('n value')
    plt.ylabel('number of multiplications')
    plt.title('Calculate Powers Algorithms')
    plt.scatter(xAxis, decByOneMults, color="red", label="decrease by one")
    plt.scatter(xAxis, decByConsMults, color="green", label="decrease by constant factor")
    plt.scatter(xAxis, divAndConqMults, color="blue", label="divide and conquer")
    plt.legend(loc = "upper left")

    plt.show()

else:
    print("Please run program again and enter either test or scatter without the ' ' ")
