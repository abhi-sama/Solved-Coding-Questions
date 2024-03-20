class Solution {
public:
    bool canFinish(int nodes, vector<vector<int>>& prerequisites) {
        vector<int> indegree(nodes,0);
    vector<vector<int>> adj(nodes);
        vector<int> topo;
        queue<int> q;
    for(auto i:prerequisites)
        adj[i[0]].push_back(i[1]);

    for(int i=0;i<nodes;i++)
    {
        for(auto it:adj[i])
        {
            indegree[it]++;
        }
    }

        for(int i=0;i<nodes;i++)
            if(indegree[i]==0)
                q.push(i);
    
    while(!q.empty())
    {
        int x=q.front();
        q.pop();
        topo.push_back(x);
        for(auto it:adj[x])
        {
            indegree[it]--;
            if(indegree[it]==0)
                q.push(it);
        }
    }
    if(topo.size()==nodes) return true;
    return false;
    }
};