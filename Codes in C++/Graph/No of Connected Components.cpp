void dfs(int i,vector<int> adjl[],vector<int> &vis,int n){
    vis[i]=1;
    for(auto adjacent:adjl[i])
    {
        if(!vis[adjacent])
            dfs(adjacent,adjl,vis,n);
    }
}

int findNumOfProvinces(vector<vector<int>>& roads, int n) {
 vector<int> adjl[n];
 for(int i=0;i<n;i++)
 {
     for(int j=0;j<n;j++)
     {
         if(roads[i][j]==1 && i!=j)
        {
            adjl[i].push_back(j);
            adjl[j].push_back(i);
        }
     }
 }

vector<int> vis(n,0);
int count=0;
for(int i=0;i<n;i++)
{
    if(!vis[i])
    {
    count++;
    dfs(i,adjl,vis,n);
    }
}
return count;
}