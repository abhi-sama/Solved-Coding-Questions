#include<queue>
int detectCycleInDirectedGraph(int nodes, vector < pair < int, int >> & edges) {
    vector<int> indegree(nodes+1,0);
   vector<vector<int>> adj(nodes+1);
    vector<int> topo;
    queue<int> q;
   for(auto i:edges)
    adj[i.first].push_back(i.second);

   for(int i=1;i<=nodes;i++)
   {
       for(auto it:adj[i])
       {
           indegree[it]++;
       }
   }

    for(int i=1;i<=nodes;i++)
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
  if(topo.size()==nodes) return 0;
   return 1;
}