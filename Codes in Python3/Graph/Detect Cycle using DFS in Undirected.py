def isCycle(src,parent,adj,vis)->bool:
    vis[src]=True
    for adjacent in adj[src]:
        if vis[adjacent] is False:
            if isCycle(adjacent,src,adj,vis):
                return True
        elif parent!=adjacent:
            return True
    return False
def cycleDetection(edges, n, m):
    vis=[False]*(n+1)
    adj=[[] for i in range(n+1)]
    for i in range(m):
        adj[edges[i][0]].append(edges[i][1])
        adj[edges[i][1]].append(edges[i][0])
    for i in range(n+1):
        if vis[i] is False:
            if isCycle(i,-1,adj, vis):
                return "Yes"
    return "No"