vector < vector < int > > nearest(vector < vector < int >> & mat, int n, int m) {
    vector < vector < int > > vis(n,vector<int>(m,0));
    vector < vector < int > > dis(n,vector<int>(m,0));
    queue<pair<pair<int,int>,int>> q;

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(mat[i][j]==1)
            {
                q.push({{i,j},0});
                vis[i][j]=1;
            }
            else
                vis[i][j]=0;
        
        }
    }
    while(!q.empty())
    {
        int row=q.front().first.first;
        int col=q.front().first.second;
        int step=q.front().second;
        q.pop();
        int dr[]={-1,0,+1,0};
        int dc[]={0,+1,0,-1};
        dis[row][col]=step;
        for(int i=0;i<4;i++)
        {
            int nrow=row+dr[i];
            int ncol=col+dc[i];
            if(nrow>=0 && nrow<n && ncol>=0 && ncol<m && vis[nrow][ncol]==0 )
            {
                vis[nrow][ncol]=1;
                q.push({{nrow,ncol},step+1});
            }
        }
    }

    return dis;
}