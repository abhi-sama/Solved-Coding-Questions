class Solution:
    def dfs(self,row:int,col:int,board: List[List[str]],vis:List[List[int]],m:int,n:int)->None:
        dr=[-1,0,+1,0]
        dc=[0,+1,0,-1]
        vis[row][col]=1
        for i in range(4):
            nrow=row+dr[i]
            ncol=col+dc[i]
            if nrow>=0 and nrow<m and ncol>=0 and ncol<n and board[nrow][ncol]=='O' and vis[nrow][ncol]==0:
                self.dfs(nrow,ncol,board,vis,m,n) 

    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        vis=[[0]*n for _ in range(m)]
        for i in range(n):
            if vis[0][i]==0 and board[0][i]=='O':
                self.dfs(0,i,board,vis,m,n)
            if vis[m-1][i]==0 and board[m-1][i]=='O':
                self.dfs(m-1,i,board,vis,m,n)

        for i in range(m):
            if vis[i][0]==0 and board[i][0]=='O':
                self.dfs(i,0,board,vis,m,n)
            if vis[i][n-1]==0 and board[i][n-1]=='O':
                self.dfs(i,n-1,board,vis,m,n)  

        for i in range(m):
            for j in range(n):
                if vis[i][j]==0 and board[i][j]=='O':
                    board[i][j]='X'      
        """
        Do not return anything, modify board in-place instead.
        """
        