class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # rows, cols= len(connections()), len(connections[0])
        adj=[[] for i in range(n)]
        for n1,n2 in connections:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        vis=set()   
        tin=[0]*n
        low=[0]*n
        critical=[]
        timer=1
        def dfs(node,parent):
            nonlocal timer
            vis.add(node)
            tin[node]=low[node]=timer
            timer+=1
            for it in adj[node]:
                if it==parent:
                    continue
                if it not in vis:
                    dfs(it,node)
                    low[node]=min(low[node],low[it])
                    if low[it]> tin[node]:
                        critical.append([it,node])
                else :
                    low[node]=min(low[node],low[it])

        dfs(0,-1)
        return critical
# TC=O(V+E)
# SC=O(V+E)
                
