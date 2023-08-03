class Solution:
    def dfs(self,V,adj,vis,res):
        vis[V]=True
        res.append(V)
        for i in adj[V]:
            if vis[i] is False:
                self.dfs(i,adj,vis,res)
                
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        res=[]
        vis=[False for i in range(V)]
        self.dfs(0,adj,vis,res)
        return res