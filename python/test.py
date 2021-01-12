#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    
    r = [0,0]
    
    for i in range(len(a)):
       
        print(a[i], b[i])
        if a[i] > b[i]:
            r[0] += 1
            print("a is bigger")
        if a[i] < b[i]:
            r[1] += 1
            print("b is bigger")
        else:
            print("banana")
    return r 

a = [5,6,7]
b = [3,6,10]

print (len(a))
print (compareTriplets(a,b))


