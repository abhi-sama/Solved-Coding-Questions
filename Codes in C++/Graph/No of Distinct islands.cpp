#include <vector>
#include <set>
void dfs(int row,int col,int** arr,vector<vector<int>> &vis,
vector<pair<int,int>> &vec,int m,int n,int row0,int col0)
{
    int delrow[]={-1,0,1,0};
    int delcol[]={0,1,0,-1};
    vis[row][col]=1;
    vec.push_back({row-row0,col-col0});
    for(int i=0;i<4;i++)
    {
        int nrow=row+delrow[i];
        int ncol=col+delcol[i];
        if(nrow>=0 && nrow<m && ncol>=0 && ncol<n &&
        vis[nrow][ncol]==0 && arr[nrow][ncol]==1)
            dfs(nrow,ncol,arr,vis,vec,m,n,row0,col0);
    }
}

int distinctIslands(int** arr, int m, int n)
{
    vector<vector<int>> vis(m,vector<int>(n,0));
    set<vector<pair<int,int>>> s;
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            if (vis[i][j]==0 && arr[i][j]==1)
            {
                vector<pair<int,int>> vec;
                //O(N*M*4)
                dfs(i,j,arr,vis,vec,m,n,i,j);
                s.insert(vec);
            }
        }
    }
    //O(N*M*log(N*M) + N*M*4)//Overall TC

    return s.size();
}