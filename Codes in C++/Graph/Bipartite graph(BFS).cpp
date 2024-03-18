class Solution {
public:
    bool bfs(int start,vector<vector<int>>& graph,vector<int> &color)
    {
        queue<int> q;
        q.push(start);
        while(!q.empty())
        {
            int node=q.front();
            q.pop();
            for(auto it:graph[node])
            {
                if(color[it]==-1)
                {
                    q.push(it);
                    color[it]=!color[node];
                }
                else{
                    if(color[it]==color[node])
                        return false;
                }

            }
        }
        return true;
    }
    bool isBipartite(vector<vector<int>>& graph) {
        int n=graph.size();
        vector<int> color(n,-1);
        color[0]=-1;
        for(int i=0;i<n;i++)
        {   if(color[i]==-1)
                if(bfs(i,graph,color)==false)
                    return false;
        }
        return true;
    }
};