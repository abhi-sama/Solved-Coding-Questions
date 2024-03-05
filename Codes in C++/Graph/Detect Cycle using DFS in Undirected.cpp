bool isCycle(int src, int parent ,vector<int> adj[], vector<int> &vis)
{
    vis[src] = 1;
        for (auto adjacent : adj[src])
        {
            if (!vis[adjacent])
            {
                if(isCycle(adjacent,src,adj,vis))
                return true;
            }
            else if (parent != adjacent)
            {
                return true;
            }
        }
    
    return false;
}

string cycleDetection(vector<vector<int>> &edges, int n, int m)
{
    vector<int> adj[n + 1];
    for (int i = 0; i < m; i++)
    {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    int v = n;
    vector<int> vis(v + 1, 0);
    for (int i = 0; i < v; i++)
    {
        if (!vis[i])
            if (isCycle(i, -1,adj, vis))
                return "Yes";
    }
    return "No";
}
