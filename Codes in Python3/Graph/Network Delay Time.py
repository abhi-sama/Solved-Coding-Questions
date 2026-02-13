# Dijkstra Approach
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=collections.defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        minHeap=[(0,k)]
        visit=set()
        t=0
        while minHeap:
            time,node= heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            t=max(t,time)
            for nei,w in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap,(w+time,nei))

        return t if len(visit)==n else -1

# TC=O(ElogV)
# SC=O(V+E)


# BFS Approach
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=collections.defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        dist={node: float('inf') for node in range(1,n+1)}
        q=deque()
        q.append((k,0))
        dist[k]=0   
        while q:
            node,time= q.popleft()
            if time>dist[node]:
                continue
            
            for nei,w in adj[node]:
                if time+w<dist[nei]:
                    dist[nei]=time+w
                    q.append((nei,time+w))

        res=max(dist.values())
        return res if res<float('inf') else -1

# TC=O(V*E)
# SC=O(V+E)


# DFS Approach
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=collections.defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        dist={node: float('inf') for node in range(1,n+1)}

        def dfs(node,time):
            if time>=dist[node]:  
                #Since if the time is arleady greater any branched starting
                #from here will reach all the branched with a delay.
                return 
            
            dist[node]=time

            for nei,w in adj[node]:
                dfs(nei,time+w)
        dfs(k,0)

        res=max(dist.values())
        return res if res<float('inf') else -1

# TC=O(V*E)
# SC=O(V+E)

#Floyd Warshall Algorithm
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf =float('inf')
        dist=[[inf]*n for _ in range(n)]

        for u,v,w in times:
            dist[u-1][v-1]=w
        
        for i in range(n):
            dist[i][i]=0 #Vertex Weight
        
        for mid in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]=min(dist[i][j], dist[i][mid]+dist[mid][j])

        res=max(dist[k-1])
        return res if res<inf else -1

# TC=O(V^3)
# SC=O(V^2)            