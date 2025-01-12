class Solution {
public:
    void dfs(int row,int col,vector<vector<char>>& board,vector<vector<int>>& vis,int m,int n)
    {
        int delrow[]={-1,0,+1,0};
        int delcol[]={0,+1,0,-1};
        vis[row][col]=1;
        for(int i=0;i<4;i++)
        {
            int nrow=row+delrow[i];
            int ncol=col+delcol[i];
            if(nrow>=0 && nrow<m && ncol>=0 && ncol<n && 
            vis[nrow][ncol]==0 && board[nrow][ncol]=='O')
               dfs(nrow,ncol,board,vis,m,n); 
        }
    }

    void solve(vector<vector<char>>& board) {
       int m=board.size();
       int n=board[0].size(); 
       vector<vector<int>> vis(m,vector<int>(n,0));
       //Traverse first and last row
       for(int i=0;i<n;i++)
       {
           if(!vis[0][i]&&board[0][i]=='O')
                dfs(0,i,board,vis,m,n);
           if(!vis[m-1][i]&&board[m-1][i]=='O')
                dfs(m-1,i,board,vis,m,n);   
       } 
       
       //Traverse first and last column
       for(int i=0;i<m;i++)
       {
           if(!vis[i][0]&&board[i][0]=='O')
                dfs(i,0,board,vis,m,n);
           if(!vis[i][n-1]&&board[i][n-1]=='O')
                dfs(i,n-1,board,vis,m,n); 
       }

       for(int i=0;i<m;i++)
       {
           for(int j=0;j<n;j++)
           {
               if(!vis[i][j]&&board[i][j]=='O')
                    board[i][j]='X';
           }
       }

    }
};