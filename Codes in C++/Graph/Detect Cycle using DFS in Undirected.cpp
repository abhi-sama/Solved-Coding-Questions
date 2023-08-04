
    bool isCycle(int node,int parent,vector<vector<int>>& adj,vector<int>& vis){
        vis[node]=1;
         for(auto adjacent:adj[node])
         {
             if(vis[adjacent]==0)
                {
                 if(isCycle(adjacent,node,adj,vis)==true)
                    return true;
                }
            else if(parent!=adjacent)
            {
                return true;
            }
         }
        
        return false;
    }

string cycleDetection (vector<vector<int>>& edges, int n, int m)
{
    vector<vector<int>> adj(n+1);
    for (int i = 0; i < m; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
    int v=n;
    vector<int> vis(v+1,0);
    for(int i=1;i<=v;i++)
    {   if(vis[i]==0)
            if(isCycle(i,-1,adj,vis)==true) 
                return "Yes";
    }
    return "No";
}
