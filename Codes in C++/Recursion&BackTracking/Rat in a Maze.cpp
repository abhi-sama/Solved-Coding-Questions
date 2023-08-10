class Solution{
    public:
    void solve(int row,int col,vector<vector<int>> &m,vector<string> &ans,vector<vector<int>> &vis,
            string s,int n,int di[],int dj[]){
            if(row==(n-1) && col==(n-1))
            { 
              ans.push_back(s); 
              return;
            }
            string dir="DLRU";
            for(int index=0;index<4;index++)
            {
                int nexti=row+di[index];
                int nextj=col+dj[index];
              if(nexti>=0&&nexti<n&&nextj>=0&&nextj<n&&!vis[nexti][nextj]&&m[nexti][nextj]!=0)
            {
                vis[row][col]=1;
                solve(nexti,nextj,m,ans,vis,s+dir[index],n,di,dj);
                vis[row][col]=0;
            }  
            }
            
    }
    vector<string> findPath(vector<vector<int>> &m, int n) {
        vector<string> ans;
        vector<vector<int>> vis(n,vector<int> (n,0));
         int di[]={1,0,0,-1};
         int dj[]={0,-1,1,0};
        if(m[0][0]==1)solve(0,0,m,ans,vis,"",n,di,dj);
        return ans;
    }
};
/*class Solution{
    public:
    void solve(int row,int col,vector<vector<int>> &m,vector<string> &ans,vector<vector<int>> &vis,string s,int n){
            if(row==(n-1) && col==(n-1)&&m[row][col]==1)
            { 
              ans.push_back(s); 
              return;
            }
            
            if(row+1<n&&!vis[row+1][col]&&m[row+1][col]!=0)
            {
                vis[row][col]=1;
                solve(row+1,col,m,ans,vis,s+"D",n);
                vis[row][col]=0;
            }
            if(col+1<n&&!vis[row][col+1]&&m[row][col+1]!=0)
            {
                vis[row][col]=1;
                solve(row,col+1,m,ans,vis,s+'R',n);
                vis[row][col]=0;
            }
            if(row-1>=0&&!vis[row-1][col]&&m[row-1][col]!=0)
            {
                vis[row][col]=1;
                solve(row-1,col,m,ans,vis,s+'U',n);
                vis[row][col]=0;
            }
            if(col-1>=0&&!vis[row][col-1]&&m[row][col-1]!=0)
            {
                vis[row][col]=1;
                solve(row,col-1,m,ans,vis,s+'L',n);
                vis[row][col]=0;
            }
    }
    vector<string> findPath(vector<vector<int>> &m, int n) {
        vector<string> ans;
        vector<vector<int>> vis(n,vector<int> (n,0));
        if(m[0][0]==1)solve(0,0,m,ans,vis,"",n);
        return ans;
    }
};*/
