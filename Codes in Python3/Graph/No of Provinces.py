from os import *
from sys import *
from collections import *
from math import *
def dfs(src,adjl,vis):
    vis[src]=True
    for adjacent in adjl[src]:
        if vis[adjacent] is False:
            dfs(adjacent,adjl,vis)
    
def findNumOfStates(roads, n):
    size=len(roads)
    vis=[False]*size
    adjl=[[] for _ in range(size)]
    for i in range(0,size):
        for j in range(0,size):
            if(roads[i][j]==1 and i!=j):
                adjl[i].append(j)
                adjl[j].append(i)
    count=0
    for i in range(0,size):
        if vis[i] is False:
            count+=1
            dfs(i,adjl,vis)
    return count
