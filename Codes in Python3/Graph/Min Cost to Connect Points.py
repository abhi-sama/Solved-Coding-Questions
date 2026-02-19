#Prim's MST Algo Optimal Approach
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N,node=len(points),0
        dist=[float('inf')]*N
        res=0
        edges=0
        visit=set()

        while edges<N-1:
            visit.add(node)
            nextNode=-1
            for i in range(N):
                    if i in visit:
                        continue
                    curDist=(abs(points[node][0]-points[i][0])+abs(points[node][1]-points[i][1]))
                    dist[i]=min(dist[i],curDist)
                    if nextNode==-1 or dist[i]<dist[nextNode]:
                        nextNode=i
            res+=dist[nextNode]
            node=nextNode
            edges+=1
        
        return res

# TC=O(n^2)
# SC=O(n)


#Prim's Algorithm
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        adj=collections.defaultdict(list)

        for i in range(len(points)):
            for j in range(i+1,len(points)):
                p1,p2=points[i], points[j]
                dist=abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
                adj[i].append([j,dist])
                adj[j].append([i,dist])

        res=0
        visit=set()
        minH=[(0,0)]
        while len(visit)<len(points):
            cost,node=heapq.heappop(minH)
            if node in visit:
                continue
            res+=cost
            visit.add(node)  
            for nei,dist in adj[node]:
                if nei not in visit:
                    heapq.heappush(minH,(dist,nei))
        return res


# TC=O(ElogV)
# SC=O(E)


#Kruskal's Algorithm
class DSU:
    def __init__(self,n): #TC=O(1)
        self.Parent=list(range(n+1))
        self.Size=[1]*(n+1)
    
    def find(self,node): #TC=O(alpha(n))
        if self.Parent[node]!=node:
            self.Parent[node]=self.find(self.Parent[node])
        return self.Parent[node]

    def union(self,u,v): #TC=O(alpha(n))
        parent_u=self.find(u)
        parent_v=self.find(v)
        if parent_u==parent_v:
            return False
        if self.Size[parent_u]<self.Size[parent_v]:
            parent_v,parent_u=parent_u,parent_v
        self.Size[parent_u]+=self.Size[parent_v]
        self.Parent[parent_v]=parent_u
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        dsu=DSU(n)
        edges=[]
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                edges.append((dist,i,j))
        
        edges.sort()
        res=0

        for dist,u,v in edges:
            if dsu.union(u,v):
                res+=dist
        
        return res

# TC=O(ElogV)
# SC=O(E)               