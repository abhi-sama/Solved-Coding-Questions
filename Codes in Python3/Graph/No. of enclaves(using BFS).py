class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        vis=[[0]*n for _ in range(m)]
        q=[]
        count=0
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    if vis[i][j]==0 and grid[i][j]==1:
                        q.append((i,j))
                        vis[i][j]=1
        while q:
            row,col=q.pop(0)
            delrow=[-1,0,1,0]
            delcol=[0,1,0,-1]
            for i in range(4):
                nrow=row+delrow[i]
                ncol=col+delcol[i]
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n and vis[nrow][ncol]==0 and grid[nrow][ncol]==1:
                    q.append((nrow,ncol))
                    vis[nrow][ncol]=1

        for i in range(m):
            for j in range(n):
                if vis[i][j]==0 and grid[i][j]==1:
                    count+=1
        return count