bool dfsCheck(int node,vector<int> adj[],vector<int>  &vis,vector<int> & pathVis)
{
	vis[node]=1;
	pathVis[node]=1;
	for(auto it:adj[node])
	{
		if(!vis[it]){
			if(dfsCheck(it,adj,vis,pathVis)==true) return true;
		}
		else if(pathVis[it])
				return true;
	}
	pathVis[node]=0;
	return false;
}

bool isCyclic(vector<vector<int>>& edges, int v, int e)
{
	vector<int> vis(v,0);
	vector<int> pathVis(v,0);
	vector<int> adj[v];
    for (auto i : edges)
        adj[i[0]].push_back(i[1]);

	for(int i=0;i<v;i++)
	{
		if(!vis[i])
			if(dfsCheck(i,adj,vis,pathVis)==true) return true;
	}
	return false;
}
