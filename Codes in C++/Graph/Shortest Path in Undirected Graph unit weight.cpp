vector<int> shortestPath(int n, vector<vector<int>>&edges, int src) {
    vector<int> adj[n];
    queue<int> q;
    for(auto it:edges)
        {
        adj[it[0]].push_back(it[1]);
        adj[it[1]].push_back(it[0]);
        }
    vector<int> dist(n,1e9);
    dist[src]=0;
    q.push(src);
    while(!q.empty())
    {   
        int node=q.front();
        q.pop();
        for(auto it:adj[node])
        {
            if(dist[node]+1<dist[it]){
                dist[it] =dist[node]+1;
                q.push(it);
            } 
        }
    }
        vector<int> ans(n, -1);
        for(int i = 0;i<n;i++) {
            if(dist[i] != 1e9) {
                ans[i] = dist[i]; 
            }
        }
        return ans; 
} 