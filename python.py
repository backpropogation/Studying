import time
import sys
import numpy as np
from decimal import  Decimal

sys.setrecursionlimit(1500)
def factorial(x):
    if x == 1 :
        return x
    elif x == 0 :
        return 1
    return x*factorial(x-1)
def facyouidiot(x):
    if x ==0:
        return 1
    elif x ==1:
        return 1
    for i in range(1, x):
        x*=i
    return x

startTime = time.clock()
print(factorial(1400))
#print(facyouidiot(1400))

endTime = time.clock()
timeElapsed =  Decimal(endTime - startTime)
print (timeElapsed)
print (len(str(factorial(1400))))
#if facyouidiot(1000)==factorial(1000):
    #print('1')
print(factorial(0),facyouidiot(0),factorial(1),facyouidiot(1))

