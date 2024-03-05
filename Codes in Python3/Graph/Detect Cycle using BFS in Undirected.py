def isCycle(src,adj,vis)->bool:
    vis[src]=True
    q=[(src,-1)]
    while q:
        node,parent=q.pop(0)
        for adjacent in adj[node]:
            if vis[adjacent] is False:
                vis[adjacent]=True
                q.append((adjacent,node))
            elif parent!=adjacent:
                return True
    return False
def cycleDetection(edges, n, m):
    vis=[False]*(n+1)
    adj=[[] for i in range(n+1)]
    for i in range(m):
        adj[edges[i][0]].append(edges[i][1])
        adj[edges[i][1]].append(edges[i][0])
    for i in range(1,n+1):
        if vis[i] is False:
            if isCycle(i, adj, vis):
                return "Yes"
    return "No"