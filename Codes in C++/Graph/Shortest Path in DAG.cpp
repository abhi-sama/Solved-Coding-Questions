void toposort(int node,vector<pair<int,int>> adj[], int vis[], stack<int> &st){
    vis[node]=1;
    for(auto it:adj[node])
    {
        if(!vis[it.first])
            toposort(it.first,adj,vis,st);
    }
    st.push(node);
}

vector<int> shortestPathInDAG(int n, int m, vector<vector<int>> &edges)
{
    vector<pair<int,int>> adj[n];
    for(auto i:edges)
        adj[i[0]].push_back({i[1],i[2]});
    int vis[n]={0};
    stack<int> st;
    for(int i=0;i<n;i++){
        if(!vis[i]){
            toposort(i,adj,vis,st);
        }
    }
    vector<int> dist(n,INT_MAX);
    dist[0]=0;
    while(!st.empty()){
        int node=st.top();
        st.pop();
        for(auto it:adj[node])
        {   int v=it.first;
            int wt=it.second;
            if(dist[node] != INT_MAX && dist[node]+wt<dist[v])
                dist[v]=dist[node]+wt;
        }
    }
    for(int i=0;i<n;i++)
        if(dist[i]==INT_MAX) dist[i]=-1;
    return dist;
}
