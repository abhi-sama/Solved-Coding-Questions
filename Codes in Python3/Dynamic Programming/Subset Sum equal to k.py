from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
    prev=[False]*(k+1)
    cur=[False]*(k+1)       
    prev[0]=cur[0]=True
    if arr[0] <= k:
        prev[arr[0]] = True
    for i in range(1,n):
        for target in range(0,k+1):
            not_take=prev[target]
            take=False
            if arr[i]<=target:
                take=prev[target-arr[i]]
            cur[target]=not_take or take
        prev=cur[:]
    return prev[k]
    pass