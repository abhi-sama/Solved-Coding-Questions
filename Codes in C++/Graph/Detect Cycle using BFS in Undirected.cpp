#include <queue>
bool isCycle(int src, vector<vector<int>> &adj, vector<int> &vis)
{
    vis[src] = 1;
    queue<pair<int, int>> q;
    q.push({src, -1});
    while (!q.empty())
    {
        int node = q.front().first;
        int parent = q.front().second;
        q.pop();
        for (auto adjacent : adj[node])
        {
            if (!vis[adjacent])
            {
                vis[adjacent] = 1;
                q.push({adjacent, node});
            }
            else if (parent != adjacent)
            {
                return true;
            }
        }
    }
    return false;
}

string cycleDetection(vector<vector<int>> &edges, int n, int m)
{
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++)
    {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    int v = n;
    vector<int> vis(v + 1, 0);
    for (int i = 1; i <= v; i++)
    {
        if (!vis[i])
            if (isCycle(i, adj, vis))
                return "Yes";
    }
    return "No";
}
