class Solution {
  public:
    // Function to return a list containing the DFS traversal of the graph.
    void dfs(int V,vector<int> adj[],vector<int> &vis,vector<int> &res){
            vis[V]=1;
            res.push_back(V);
        for (auto it:adj[V])
            if(!vis[it])
            dfs(it,adj,vis,res);
        
            
    }
    vector<int> dfsOfGraph(int V, vector<int> adj[]) {
        vector<int> res;
        vector<int> vis(V,0);
        dfs(0,adj,vis,res);
        return res;
    }
};