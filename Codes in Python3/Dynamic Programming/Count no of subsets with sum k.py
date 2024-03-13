from typing import List

def findWays(arr: List[int], k: int) -> int:
    n=len(arr)
    prev=[0]*(k+1)
    cur=[0]*(k+1)       
    prev[0]=cur[0]=1
    if arr[0] <= k:
        prev[arr[0]] = 1
    for i in range(1,n):
        for target in range(1,k+1):
            not_take=prev[target]
            take=0
            if arr[i]<=target:
                take=prev[target-arr[i]]
            cur[target]=not_take + take
        prev=cur[:]
    return prev[k]
    pass