class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
    int nodes=graph.size();
    vector<int> indegree(nodes,0);
    vector<vector<int>> adjRev(nodes);
    vector<int> topo;
    queue<int> q;
        //Reverse the graph
    for(int i=0;i<nodes;i++)
    {
        for(auto it:graph[i])
        {
            adjRev[it].push_back(i);
            indegree[i]++;
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
        for(auto it:adjRev[x])
        {
            indegree[it]--;
            if(indegree[it]==0)
                q.push(it);
        }
    }
    sort(topo.begin(),topo.end());
    return topo;   
    }
};