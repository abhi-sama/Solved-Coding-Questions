#Topological Sort (Kahn's Algorithm) Approach
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        indegree=[0]*(n+1)
        adj = [[] for _ in range(n + 1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u]+=1
            indegree[v]+=1

        q=deque()
        for i in range(1,n+1):
            if indegree[i]==1:
                q.append(i)

        while q:
            node=q.popleft()
            indegree[node]-=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==1:
                    q.append(nei)

        for u,v in reversed(edges):
            if indegree[u]==2 and indegree[v]==2:
                return [u,v]
        return []

# TC=O(E+V)
# SC=O(E+V)

#Using DFS Approach
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        adj=[[] for _ in range(n+1)]

        def dfs(node,par):
            if visit[node]:
                return True
            visit[node]=True
            for nei in adj[node]:
                if nei==par:
                    continue
                if dfs(nei,node):
                    return True
            return False

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit=[False]*(n+1)
            if dfs(u,-1):
                return [u,v]
        return []

# TC=O(E*(E+V))
# SC=O(E+V)