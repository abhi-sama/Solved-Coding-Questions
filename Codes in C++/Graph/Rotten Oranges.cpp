class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
       int m=grid.size();
       int n=grid[0].size();
       int vis[m][n];
       int fresh_cnt=0;
       queue<pair<pair<int,int>,int>> q;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(grid[i][j]==2)
                  {
                      q.push({{i,j},0});
                      vis[i][j]=1;
                  }
                else{
                    vis[i][j]=0;
                }
            if(grid[i][j]==1) fresh_cnt++;
            }
        }
        int tm=0;
        int dr[]={-1,0,+1,0};
        int dc[]={0,+1,0,-1};
        int cnt=0;
        while(!q.empty()){
        int r=q.front().first.first;
        int c=q.front().first.second;
        int t=q.front().second;
        q.pop();
        tm=max(tm,t);
        for(int i=0;i<4;i++){
        int nrow=r+dr[i];
        int ncol=c+dc[i];
        if(nrow>=0&&nrow<m&&ncol>=0&&ncol<n&&vis[nrow][ncol]==0&&grid[nrow][ncol]==1)
        {
            q.push({{nrow,ncol},t+1});
            vis[nrow][ncol]=1;
            cnt++;
        }
        }
        }
        if(cnt!=fresh_cnt) return -1;
        return tm;
        }
};