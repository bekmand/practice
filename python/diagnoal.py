import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    

    n = len(arr)
    first_diag_sum = sum(arr[i][i] for i in range (len(arr)))
    second_diag_sum = sum(arr[i][len(arr)-i-1] for i in range (len(arr)))

    return first_diag_sum

arr = [[1,2,3],[4,5,6],[7,8,9]]

#print(len(arr))

print(diagonalDifference(arr))
