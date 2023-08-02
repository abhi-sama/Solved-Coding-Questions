class Solution {
  public:
    // Function to return Breadth First Traversal of given graph.
    vector<int> bfsOfGraph(int V, vector<int> adj[]) {
       vector<int> vis(V,0);
       vector<int> bfs;
       queue<int> q;
       vis[0]=1;
       q.push(0);
       while(!q.empty()){
           int x=q.front();
           q.pop();
           bfs.push_back(x); 
           for(auto it:adj[x]){
           if(vis[it]==0)
           {
            vis[it]=1;
            q.push(it);
           }
           }
       }
       return bfs;
    }
};