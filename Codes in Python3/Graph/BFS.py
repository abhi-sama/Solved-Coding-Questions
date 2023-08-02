from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        bfs=[]
        vis=[False for i in range(V)]
        q=[0]
        vis[0]=True
        while q:
            x=q.pop(0)
            bfs.append(x)
            for i in adj[x]:
                if vis[i]==False:
                    vis[i]=True
                    q.append(i)
        return bfs