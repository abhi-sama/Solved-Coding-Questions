class Solution {
public:
bool dfsCheck(int node, vector<int> adj[], vector<int> &vis,
              vector<int> &pathVis, vector<int> &check) {
    vis[node] = 1;
    pathVis[node] = 1;
    check[node] = 0; // Mark current node as safe initially
    for (auto it : adj[node]) {
        if (!vis[it]) {
            if (dfsCheck(it, adj, vis, pathVis, check))
            {
                check[node] = 0; // Mark current node as unsafe if cycle detected
                return true;
            }
            }
        else if (pathVis[it]) {
            check[node] = 0; // Mark current node as unsafe if cycle detected
            return true;
        }
    }
    check[node]=0;
    pathVis[node] = 0;
    return false;
}

    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int v=graph.size();
        vector<int> vis(v,0);
        vector<int> pathVis(v,0);
        vector<int> check(v,0);
        vector<int> adj[v];
        vector<int> res;

        for (auto i : graph)
            adj[i[0]].push_back(i[1]);

        for(int i=0;i<v;i++)
        {
            if(!vis[i])
                dfsCheck(i,adj,vis,pathVis,check);
        }
        for(int i=0;i<v;i++)
        {
            if(check[i])
                res.push_back(i);
        }
        return res;
    }
};