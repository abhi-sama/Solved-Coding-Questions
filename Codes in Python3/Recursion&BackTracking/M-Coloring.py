from typing import *
def isValid(node:int,mat: List[List[int]], color: List[int], n: int,col: int) -> bool:
    for i in range(0,n):
        if i!=node and mat[i][node]==1 and color[i]==col:
            return False
    return True

def solve(node:int,mat: List[List[int]], color: List[int], n: int,m: int) -> bool:
    if node==n:
        return True
    for i in range(1,m+1):
        if isValid(node,mat,color,n,i):
            color[node]=i
            if solve(node+1,mat,color,n,m):
                return True
            color[node]=0
    return False


def graphColoring(mat: List[List[int]], m: int) -> str:
    n=len(mat)
    color = [0]*n
    if solve(0,mat,color,n,m):
        return "YES"
    else:
        return "NO"
    pass 