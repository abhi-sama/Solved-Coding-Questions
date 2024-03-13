from typing import List
def minSubsetSumDifference(arr: List[str], n: int) -> int:
    total_sum=sum(arr)
    k=total_sum
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
    mini=float('inf')
    for i in range(0,k+1):
        if prev[i]:
            s1=i
            s2=total_sum-i
            mini=min(mini,abs(s1-s2))
    return mini
    pass