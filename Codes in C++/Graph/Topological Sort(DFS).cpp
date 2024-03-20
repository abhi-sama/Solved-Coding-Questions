#include<stack>
void dfs(int node,vector<int> &vis,vector<vector<int>> &adj,stack<int> &s)
{
    vis[node]=1;
    for(auto it:adj[node])
    {
        if(!vis[it])
            dfs(it,vis,adj,s);
    }
    s.push(node);
}

vector<int> topologicalSort(vector<vector<int>> &graph, int edges, int nodes) {
   vector<int> vis(nodes,0);
   stack<int> s;
   vector<vector<int>> adj(nodes);
   for(auto i:graph)
    adj[i[0]].push_back(i[1]);
   for(int i=0;i<nodes;i++)
   {
       if(!vis[i])
        dfs(i,vis,adj,s);
   }
   vector<int> ans;
   while(!s.empty())
   {
       ans.push_back(s.top());
       s.pop();
   }
   return ans;
}
