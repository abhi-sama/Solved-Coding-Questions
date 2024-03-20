vector<int> topologicalSort( vector<int> adj[], int nodes) {
   vector<int> indegree(nodes,0);
    vector<int> topo;
    queue<int> q;

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

   return topo;
}
string getAlienLanguage(vector<string> &dictionary, int k)
{   
    vector<int> adj[k];   
    int n=dictionary.size();
    for(int i=0;i<n-1;i++)
    {
        string s1=dictionary[i];
        string s2=dictionary[i+1];
        int len=min(s1.length(),s2.length());
        for(int j=0;j<len;j++)
        {
            if(s1[j]!=s2[j])
            {
                adj[s1[j]-'a'].push_back(s2[j]-'a');
                break;
            }
        }
    }
    vector<int> topo=topologicalSort(adj,k);
    string ans="";
    for(auto it:topo)
        ans=ans+char(it+'a');
    return ans;
}