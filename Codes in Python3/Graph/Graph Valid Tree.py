#DFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj=[[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit=set()

        def dfs(node,parent):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei==parent:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        
        return dfs(0,-1) and len(visit)==n

# TC=O(E+V)
# SC=O(E+V)

#BFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj=[[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit=set()

        q=deque()
        q.append((0,-1))
        visit.add(0)
        while q:
            node,parent=q.popleft()
            for nei in adj[node]:
                if nei==parent:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei,node))
        return  len(visit)==n
# TC=O(E+V)
# SC=O(E+V)